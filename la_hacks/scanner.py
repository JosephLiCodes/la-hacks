import reflex as rx
from la_hacks.state import State

@rx.page(title="EcoScan | Scanner")
def scanner() -> rx.Component:
    html_content = """
   <!doctype html>
<html lang="en">

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <style>
    body, html {
        margin: 0;
        padding: 0;
        height: 100%;
        overflow: hidden; /* Hide scrollbars */
        display: flex;
        justify-content: center;
        align-items: center;
    }
    video {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        object-fit: cover; /* This will cover the full screen, cropping the video if necessary */
    }
    .scanner-box {
        width: 60vw; /* 60% of the viewport width */
        height: 15vh; /* 30% of the viewport height */
        border: 5px dashed #ffffff7f;
        border-radius: 10px; 
        position: relative;
        display: flex;
        justify-content: center;
        align-items: center;
    }
  </style>
</head>

<body>
<video id="video"></video>
<div class="scanner-box"></div>

<script type="text/javascript" src="https://unpkg.com/@zxing/library@latest/umd/index.min.js"></script>
<script type="text/javascript">
  window.addEventListener('load', function () {
    let selectedDeviceId;
    const codeReader = new ZXing.BrowserMultiFormatReader()
    console.log('ZXing code reader initialized')
    codeReader.listVideoInputDevices()
      .then((videoInputDevices) => {
        const sourceSelect = document.getElementById('sourceSelect')
        selectedDeviceId = videoInputDevices[0].deviceId

        codeReader.decodeFromVideoDevice(selectedDeviceId, 'video', (result, err) => {
            if (result) {
              console.log(result.text)
              // handle result
              window.location.href = "/results/" + result
            }
            if (err && !(err instanceof ZXing.NotFoundException)) {
              console.error(err)
              // handle result
            }
          })
          console.log(`Started continous decode from camera with id ${selectedDeviceId}`)

      })
      .catch((err) => {
        console.error(err)
      })
  })
</script>
</body>
</html>
    """
    return rx.html(html_content)