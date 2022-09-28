# collimate_points

Functions for collimating points on images (or set of images) and giving sub-pixel accurate image coordinates

## Setup

Python: You need Python 3.8. We recommend the Anaconda distribution because it includes all the required libraries. When installing, if asked whether the installer should initialize Anaconda3, say "yes". Anaconda must be initialized upon install such that python can be called from the command line. A way to check is to simply enter python at your command prompt and see if the resulting header info includes Anaconda and Python 3. If it doesn't, you may still need to initialize your Conda install.

Metashape: You must install the Metashape Python 3 module (Metashape version 1.8). Download the [current .whl file](https://www.agisoft.com/downloads/installer/) and install it following [these instructions](https://agisoft.freshdesk.com/support/solutions/articles/31000148930-how-to-install-metashape-stand-alone-python-module) (using the name of the .whl file that you downloaded).

## License

Metashape license: You need a license (and associated license file) for Metashape. The easiest way to get the license file (assuming you own a license) is by installing the Metashape Professional Edition GUI software (distinct from the Python module) and registering it following the prompts in the software (note you need to purchase a license first). Once you have a license file (whether a node-locked or floating license), you need to set the agisoft_LICENSE environment variable (search onilne for instructions for your OS; look for how to permanently set it) to the path to the folder containing the license file (metashape.lic).

### Setup agisoft_LICENSE environment variable for floating license

Set permanently: 

```bash
sudo nano ~/.bashrc
```

add the line

```bash
export agisoft_LICENSE="port"@"address"
```

(replace port and address with your values)

```bash
source ~/.bashrc
```

check if the new environment is present:

```bash
end
```
