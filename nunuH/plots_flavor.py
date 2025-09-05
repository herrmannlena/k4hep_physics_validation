
import ROOT

# global parameters
intLumi        = 1.
intLumiLabel   = "L = 10.8 ab^{-1}"
ana_tex        = 'e^{+}e^{-} #rightarrow #nunu H'
delphesVersion = '3.4.2'
energy         = 240.0
collider       = 'FCC-ee'
formats        = ['png','pdf']

#outdir         = './outputs/plots/flavor/' 
#inputDir       = './outputs/histmaker/flavor/' 

outdir         = '/afs/cern.ch/work/l/lherrman/public/k4hep_physics_validation/nunuHoutput/plots' 
# inputDir       = '/afs/cern.ch/work/s/saaumill/public/MyFCCAnalyses/outputs/histmaker_fullsim/ZHgamma_btag/' 
inputDir       = '/afs/cern.ch/work/l/lherrman/public/k4hep_physics_validation/nunuH/output/histmaker'

plotStatUnc    = True

colors = {}
colors['nunuH'] = ROOT.kRed


procs = {}
procs['signal'] = {'nunuH':['p8_ee_ZnunuHbb_ecm240']}
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
    "xtitle":   ["All events", "b_score_sum > 1.6"], #  "120 < m_{recoil} < 132 "], # "110 < m_{recoil} < 140 "
    "ytitle":   "Events ",
}

# hists["gamma_recoil_m"] = {
#     "input":   "gamma_recoil_m",
#     "output":   "gamma_recoil_m",
#     "logy":     False,
#     "stack":    True,
#     "xmin":     110,
#     "xmax":     150,
#     "xtitle":   "Recoil (GeV)",
#     "ytitle":   "Events ",
#     "density": False,
#     "scaleSig": 1000,

# }


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

hists["mcID"] = {
    "input":   "mcID",
    "output":   "mcID",
    "logy":     True,
    "stack":    True,
    "xmin":     0,
    "xmax":     40,
    "xtitle":   "mcID",
    "ytitle":   "Events ",
    "density": False,

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
