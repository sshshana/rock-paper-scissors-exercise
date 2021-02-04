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

## Setup

In in the root directory of your local repository, create a new file called ".env", and update the contents of the ".env" file to specify your desired username:

    USER_NAME="John Snow"

> NOTE: If you don't customize your user name, it will be set as "Playser One" by default.

## Usage

Run the game script:

```py
python game.py