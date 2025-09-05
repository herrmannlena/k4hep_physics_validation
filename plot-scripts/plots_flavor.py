import os, copy
import ROOT

import sys

print(len(sys.argv))
# exit()

if len(sys.argv) < 6:
    raiseException("Missing command line arguments!")
else: 
    print("Running with process_name", sys.argv[4])
    process_name = sys.argv[4]

    print("Running with plotDir", sys.argv[5])
    plotDir = sys.argv[5]


def extract_between_underscores(process_name):
    parts = process_name.split("_")
    if len(parts) < 3:
        raise ValueError(f"Process name '{process_name}' must contain at least two underscores")
    return parts[1]



# parser = argparse.ArgumentParser(description="My script that takes a variable")
# parser.add_argument( "--xsec", type=str, required=True, help="cross-section")
# parser.add_argument( "--ilum", type=str, required=True, help="integrated-luminosity")
# parser.add_argument( "--ecm", type=str, required=True, help="integrated-luminosity")
# parser.add_argument( "--process_name", type=str, required=True, help="process name")
# parser.add_argument( "--output", type=str, required=True, help="output directory")

# args = parser.parse_args()

# process_name = "wzp6_ee_nunuH_ecm240"


# global parameters
intLumi = 1.
intLumiLabel   = "L = 10.8 ab^{-1}"
ana_tex        = 'e^{+}e^{-} #rightarrow #nunu H'
#below doesn't work yet
# intLumiLabel   = "L = {{}} ab^{-1}".format(intLumi*1e-6) 
# ana_tex        = 'e^{+}e^{-} #rightarrow {}'.format(extract_between_underscores(process_name))
delphesVersion = '3.4.2'
energy         = 240
collider       = 'FCC-ee'
formats        = ['png','pdf']


#outdir         = './outputs/plots/flavor/' 
#inputDir       = './outputs/histmaker/flavor/' 

outdir         = os.path.join(plotDir, "plots")
# inputDir       = '/afs/cern.ch/work/s/saaumill/public/MyFCCAnalyses/outputs/histmaker_fullsim/ZHgamma_btag/' 
inputDir       = os.path.join(plotDir, "hists")

plotStatUnc    = True

colors = {}
colors['nunuH'] = ROOT.kRed


procs = {}
procs['signal'] = {'nunuH':[process_name]}
procs['backgrounds'] =  {'':[], }


legend = {}
legend['nunuH'] = '#nunu H'



hists = {}
hists2D = {}




hists["cutFlow"] = {
    "input":   "cutFlow",
    "output":   "cutFlow",
    "logy":     True,
    "stack":   True,
    "xmin":     0,
    "xmax":     2,
    "xtitle":   ["All events", "b_score_sum > 1.6"], 
    "ytitle":   "Events ",
}


hists["b_tags_sum"] = {
    "input":   "b_tags_sum",
    "output":   "b_tags_sum",
    "logy":     True,
    "stack":    True,
    "xmin":     0,
    "xmax":     2,
    "xtitle":   "b-tags sum",
    "ytitle":   "Events ",
    "density": False,
    "scaleSig": 1000,
    "rebin": 2,

}

hists["m_jj"] = {
    "input":   "m_jj",
    "output":   "m_jj",
    "logy":     True,
    "stack":    True,
    "xmin":     0,
    "xmax":     240,
    "xtitle":   "m_jj",
    "ytitle":   "Events ",
    "density": False,
    "scaleSig": 1000,

}


hists["missingMass"] = {
    "input":   "missingMass",
    "output":   "missingMass",
    "logy":     True,
    "stack":    True,
    "xmin":     0,
    "xmax":     250,
    "xtitle":   "missingMass",
    "ytitle":   "Events ",
    "density": False,

}
