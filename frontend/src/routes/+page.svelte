<script lang="ts">
  import { onMount } from "svelte";
  import Result from "$lib/Result.svelte";
  import Countdown from "$lib/Countdown.svelte";
  import { writable } from "svelte/store";
  import { fade } from "svelte/transition";

  console.log("Royal Hackaway");

  let videoElement: HTMLVideoElement;
  let canvasElement: HTMLCanvasElement;
  // let photoElement: HTMLImageElement;

  // onMount basically means "start when the DOM is loaded"
  onMount(() => {
    // Boilerplate code to get the video stream from the camera
    navigator.mediaDevices
      .getUserMedia({ video: true })
      .then((stream) => {
        videoElement.srcObject = stream;
        videoElement.onloadedmetadata = videoElement.play;
      })
      .catch(console.error);
  });

  const takePicture = () => {
    const context = canvasElement.getContext("2d")!;
    context.drawImage(
      videoElement,
      0,
      0,
      canvasElement.width,
      canvasElement.height
    );

    // We need to send this to the backend
    const data = canvasElement.toDataURL("image/png");

    console.log("A Picture has been taken!");
    // photoElement.setAttribute("src", data)
  };
  let isDone = writable(false);

  isDone.subscribe((done) => {
    if (done) {
      takePicture();
    }
  });
</script>

<div>
  <Result />
</div>

<div class="flex flex-col w-full h-full items-center justify-center">
  <canvas
    style:display={$isDone ? "block" : "none"}
    width={512}
    height={390}
    bind:this={canvasElement}
  ></canvas>
  {#if $isDone === false}
    <video width={512} bind:this={videoElement}>
      <track kind="captions" src="" />
    </video>
    <br />
    <Countdown bind:isDone={$isDone} />
  {:else}
    <p transition:fade class="font-bold text-4xl p-2">Picture has been sent!</p>
  {/if}
</div>

<Countdown bind:isDone={$isDone} />
