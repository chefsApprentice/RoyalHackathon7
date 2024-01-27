<script lang="ts">
    import { onMount } from "svelte";
    import Result from "$lib/Result.svelte";
  import Countdown from "$lib/Countdown.svelte";
    import { writable } from "svelte/store";

    console.log("Royal Hackaway");

    let videoElement: HTMLVideoElement;
    let canvasElement: HTMLCanvasElement;
    // let photoElement: HTMLImageElement;

    // onMount basically means "start when the DOM is loaded"
    onMount(() => {
        // Boilerplate code to get the video stream from the camera
        navigator.mediaDevices.getUserMedia({ video: true })
            .then((stream) => {
                videoElement.srcObject = stream;
                 videoElement.onloadedmetadata = videoElement.play;
            })
            .catch(console.error)
    })

    const takePicture = () => {
        // do capture stuff

        const context = canvasElement.getContext("2d")!;
        context.drawImage(videoElement, 0, 0, canvasElement.width, canvasElement.height);

        const data = canvasElement.toDataURL("image/png");
        // photoElement.setAttribute("src", data)
    }
    let isDone = writable(false);

    isDone.subscribe((done) => {
        if (done) {
            takePicture();
        }
    });
</script>

<div>
    <Result/>
    <Countdown bind:isDone={$isDone} />
</div>

<!--<button on:click={takePicture}>Take Picture</button>-->
<!--<img src="" alt="A picture of you!"/>-->
<video width={256} height={500} bind:this={videoElement}>
    <track kind="captions" src=""/>
</video>
<canvas width={256} height={200} bind:this={canvasElement}></canvas>

