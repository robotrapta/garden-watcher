# Deer Bark

Uses [Groundlight](https://pypi.org/project/groundlight/) to detect the presence of
any animals in the scene, and if it sees one it plays a sound of a barking dog.

# Setting up

## Groundlight account setup

You can use a free Groundlight account.  Then get a 
[Groundlight API token](https://code.groundlight.ai/python-sdk/docs/getting-started/api-tokens) and save it as an environment variable:

```
export GROUNDLIGHT_API_TOKEN="api_..."
```

## Camera configuration and preview

You need to customize the `framegrab.yaml` file to point to the correct camera.
See [framegrab](https://github.com/groundlight/framegrab) for reference, but this
file is a pretty good starting point.  You can add cropping and other settings
to the yaml file to get the best results.

To preview if the camera config is working properly:

```
framegrab preview ./framegrab.yaml
```

The in-terminal preview requires an advanced terminal program such as
[iTerm2](https://iterm2.com/).

Note that you can include secrets with environment variable substitution
like `{{CAMERA_PASSWORD}}`.  You can set these in your shell before running
the app.


## Running the python program

Install the dependencies with pip:

```
pip install -r requirements.txt
```

Then run the app:

```
python app.py
```


## Hardware

I used a Raspberry Pi 4 with a camera module.  You can use any camera that
works with the [framegrab](https://github.com/groundlight/framegrab) library.

For easy set-up, you can use Groundlight's [pre-built Raspberry Pi images](https://github.com/groundlight/groundlight-pi-gen).

https://hub.docker.com/r/groundlight/groundlight-raspberry-pi-camera

