# k4hep_physics_validation

## Getting Started

0. Clone the repository:

```bash
git clone https://github.com/herrmannlena/k4hep_physics_validation.git
cd k4hep_physics_validation
```

1. Edit `ci-scripts/config.cfg` to point to your own `Key4HEP` stack and set the number of events (NO SPACES):

   ```bash
   # config.cfg
   KEY4HEP_SETUP="/cvmfs/sw-nightlies.hsf.org/key4hep/setup.sh"
   NUMBER_OF_EVENTS=10
   ```
2. Run the pipeline:
```bash
    source setup.sh
```

The output files will be generated in a new directory called `output_data`.




