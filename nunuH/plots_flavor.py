
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

outdir         = '/afs/cern.ch/work/l/lherrman/private/k4hepphyscal/fccanalysis/nunuH/output/plots' 
# inputDir       = '/afs/cern.ch/work/s/saaumill/public/MyFCCAnalyses/outputs/histmaker_fullsim/ZHgamma_btag/' 
inputDir       = '/afs/cern.ch/work/l/lherrman/private/k4hepphyscal/fccanalysis/nunuH/output/histmaker'

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




"""
hists["cutFlow"] = {
    "input":   "cutFlow",
    "output":   "cutFlow",
    "logy":     True,
    "stack":   True,
    "xmin":     0,
    "xmax":     8,
    "ymin":     1e4,
    "ymax":     1e11,
    #"xtitle":   ["All events", "iso < 0.2", "60  < p_{#gamma} < 100 ", "|cos(#theta)_{#gamma}|<0.9", "n particles > 5"],
    "xtitle":   ["All events"], #  "120 < m_{recoil} < 132 "], # "110 < m_{recoil} < 140 "
    "ytitle":   "Events ",
}
"""
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
