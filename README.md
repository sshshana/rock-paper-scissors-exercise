# Rock Paper Scissors Game

With this application, you can play a rock-paper-scissors game with a computer.

## Prerequisites

  + Anaconda 3.7+
  + Python 3.7+
  + Pip

## Installation

Fork this [remote repository](https://github.com/sshshana/rock-paper-scissors-exercise) under your own control, then "clone" or download your remote copy onto your local computer. Choose a familiar download location like the Desktop.

Then navigate there from the command line (subsequent commands assume you downloaded the remote copy onto the Desktop):

```sh
cd ~/Desktop/rock-paper-scissors-exercise
```

Use Anaconda to create and activate a new virtual environment, perhaps called "my-game-env":

```sh
conda create -n my-game-env python=3.8
conda activate my-game-env
```

From inside the virtual environment, install package dependencies:

```sh
pip install -r requirements.txt
```

> NOTE: if this command throws an error like "Could not open requirements file: [Errno 2] No such file or directory", make sure you are running it from the repository's root directory, where the requirements.txt file exists (see the initial `cd` step above)

## Setup

In in the root directory of your local repository, create a new file called ".env", and update the contents of the ".env" file to specify your desired player name. Please see the exmaple below:

    PLAYER_NAME="John Snow"

> NOTE: If you don't customize your user name, it will be set as "Playser One" by default.

## Usage

Run the game script:

```py
python game.py
```

> NOTE: if you see an error like "ModuleNotFoundError: No module named '...'", it's because the given package isn't installed, so run the `pip` command above to ensure that package has been installed into the virtual environment