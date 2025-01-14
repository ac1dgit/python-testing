#  *.conda installs (python 3.9.2)*
>`conda install -c conda-forge cudatoolkit=11.2 cudnn=8.1.0`\
>`python.exe -m pip install --upgrade pip`\
>`pip install --upgrade setuptools`\
>`pip install "numpy<2.0.0"`\
>`pip install "tensorflow<2.11"`\
>`pip install "matplotlib"`

## confirm tensor
>`python -c "import tensorflow as tf; print(tf.reduce_sum(tf.random.normal([1000, 1000])))"`

## confirm gpu list
>`python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"`

# *.conda for pi*
>`wget <https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-aarch64.sh>`\
>`bash Miniforge3-Linux-aarch64.sh`\
>`conda --version`
## create conda env python 3.9 in vscode
>`pip install "numpy<2.0.0"`\
>`pip install "tensorflow<2.15"`\
>`pip install "matplotlib"`

## mcc118 lib install
# in pi terminal
>`cd ~`\
>`git clone https://github.com/mccdaq/daqhats.git`\
>`cd ~/daqhats`\
>`sudo ./install.sh`
# in vscode
>`pip install daqhats`

## lgpio stuff
>`pip install spidev`\
>`pip install rpi-lgpio`