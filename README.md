# Deer Bark

When it sees a deer, it barks.


## Setting up

You need to customize the `framegrab.yaml` file to point to the correct camera.
See [framegrab](https://github.com/groundlight/framegrab) for reference, but this
file is a pretty good starting point.  You can add cropping and other settings
to the yaml file to get the best results.

To preview if the camera config is working properly:

```
framegrab preview ./framegrab.yaml
```

Note that you can include secrets with environment variable substitution
like `{{CAMERA_PASSWORD}}`.  You can set these in your shell before running
the app.
