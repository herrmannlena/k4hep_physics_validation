# from Lena 11.April 2025, see: https://github.com/herrmannlena/FCCAnalyses/blob/higgsgamma/myanalysis/histmaker_recoil.py 

import os, copy

import sys

print(len(sys.argv))
# exit()

if len(sys.argv) < 6:
    raiseException("Missing command line arguments!")
else: 
    print("Running with sample", sys.argv[4])
    sample = sys.argv[4]

    print("Running with outputDir", sys.argv[5])
    outputDir = sys.argv[5]

# list of processes (mandatory)
processList = {
    sample: {'fraction':1, 'inputDir': "" },  #what are the exact values here?/ correct cross section
}

includePaths = ["functions.h"]
nCPUS       = -1

doScale = True
intLumi = 1.

# Link to the dictionary that contains all the cross section information etc...
procDict = "FCCee_procDict_spring2021_IDEA.json"

# Add MySample_p8_ee_ZH_ecm240 as it is not an offical process
procDictAdd = {sample: {"numberOfEvents": 10, "sumOfWeights": 10, "crossSection": 1.0, "kfactor": 1.0, "matchingEfficiency": 1.0}}



# define some binning for various histograms
bins_a_p = (100, 0, 500) # 100 MeV bins
bins_a_n = (10, 0, 10) # 100 MeV bins

bins_count = (10, 0, 10)


##?| name of collections in EDM root files
collections = {
    "GenParticles": "Particle",
    "PFParticles": "ReconstructedParticles",
    "PFTracks": "EFlowTrack",
    "PFPhotons": "EFlowPhoton",
    "PFNeutralHadrons": "EFlowNeutralHadron",
    # "TrackState": "EFlowTrack_1",
    "TrackState": "_EFlowTrack_trackStates",
    "TrackerHits": "TrackerHits",
    "CalorimeterHits": "CalorimeterHits",
    # "dNdx": "EFlowTrack_2",
    "dNdx": "_EFlowTrack_dxQuantities",
    "PathLength": "EFlowTrack_L",
    "Bz": "magFieldBz",
    "Electrons": "Electron",
    "Muons": "Muon",
}



# build_graph function that contains the analysis logic, cuts and histograms (mandatory)
def build_graph(df, dataset):

    results = []
    df = df.Define("weight", "1.0")
    weightsum = df.Sum("weight")

    # full sim defines

    # in FullSim, both the reco and gen particles are produced with a crossing angle
    df = df.Define("ReconstructedParticles", "FCCAnalyses::unBoostCrossingAngle(PandoraPFOs, -0.015)")

    df = df.Define("jets_p4", "FCCAnalyses::return_p4_jets(RefinedVertexJets)") # recoil mass
    df = df.Define("m_jj", "JetConstituentsUtils::InvariantMass(jets_p4[0], jets_p4[1])")
    results.append(df.Histo1D(("m_jj", "", 100, 0, 240), "m_jj"))

    df = df.Define("missingMass", "FCCAnalyses::ZHfunctions::missingMass(240., ReconstructedParticles)")
    results.append(df.Histo1D(("missingMass", "", 250, 0, 250), "missingMass"))

    df = df.Define("b_tags_sum", "b_tags[0] + b_tags[1]") # sum of b-tag scores 
    results.append(df.Histo1D(("b_tags_sum", "", 100, 0, 2), "b_tags_sum"))

    #########
    ### CUT 0: all events
    #########
    df = df.Define("cut0", "0")
    results.append(df.Histo1D(("cutFlow", "", *bins_count), "cut0"))

    #########
    ### CUT 1: b-score cut
    #########
    df = df.Filter("b_tags_sum > 1.6") 
    df = df.Define("cut1", "1")
    results.append(df.Histo1D(("cutFlow", "", *bins_count), "cut1"))


    return results, weightsum
