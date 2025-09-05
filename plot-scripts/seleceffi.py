# determine the selection efficiencies
import ROOT
import argparse

parser = argparse.ArgumentParser(description="variables for efficiency determination")
parser.add_argument( "--inputFile", type=str, required=False, default="../output/", help="Histmaker output file to extract cutFlow counts")

args = parser.parse_args()

# Open the ROOT file
input_file = args.inputFile
f = ROOT.TFile.Open(input_file )
if not f or f.IsZombie():
    raise RuntimeError("Could not open file")

# Get the histogram 
histo = f.Get("cutFlow")   
if not histo:
    raise RuntimeError("Could not retrieve histogram 'cutFlow'")

# Find first and last filled bins
first_bin = -1
last_bin = -1
nbins = histo.GetNbinsX()

for ibin in range(1, nbins + 1):  # skip underflow/overflow
    if histo.GetBinContent(ibin) > 0:
        if first_bin == -1:
            first_bin = ibin
        last_bin = ibin

if first_bin == -1:
    print("Histogram has no filled bins")
else:
    print(f"First filled bin: {first_bin}, content = {histo.GetBinContent(first_bin)}")
    print(f"Last filled bin: {last_bin}, content = {histo.GetBinContent(last_bin)}")

# selection efficiency
eff = histo.GetBinContent(last_bin) / histo.GetBinContent(first_bin)
print(f"Efficiency: {eff:.4f}")
