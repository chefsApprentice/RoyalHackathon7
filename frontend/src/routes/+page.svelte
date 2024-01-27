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

  let sendData = async (data: any) => {
    await fetch("http://localhost:3000/img", {
      method: "POST",
      body: data,
    });
  };

  // onMount basically means "start when the DOM is loaded"
  onMount(async () => {
    // Boilerplate code to get the video stream from the camera

    try {
      videoElement.srcObject = await navigator.mediaDevices.getUserMedia({
        video: true,
      });
      videoElement.onloadedmetadata = videoElement.play;
    } catch (error) {
      console.error(error);

      switch (error) {
        default:
        case "DOMException: Permission denied":
          videoError.set("Please enable webcam permissions on this site!");
          break;
      }
    }
  });

  let res = writable(0);
  let resRecieved = writable(false);

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
    console.log("data:" + data);
    sendData(data);

    console.log("A Picture has been taken!");
    // photoElement.setAttribute("src", data)
  };

  let isDone = writable(false);
  let videoError = writable("");

  isDone.subscribe((done) => {
    if (done) {
      takePicture();
    }
  });
</script>

<div class="flex flex-col w-full h-full items-center justify-center">
  <canvas
    style:display={$isDone ? "block" : "none"}
    width={512}
    height={390}
    bind:this={canvasElement}
  ></canvas>
  {#if $isDone === false}
    {#if $videoError}
      <p
        class="bg-red-500 shadow-lg shadow-red-500/20 text-white text-2xl p-3 m-3 rounded"
      >
        {$videoError}
      </p>
    {:else}
      <video width={512} bind:this={videoElement}>
        <track kind="captions" src="" />
      </video>
      <br />
      <Countdown bind:isDone={$isDone} />
    {/if}
  {:else if $resRecieved == false}
    <p transition:fade class="font-bold text-4xl p-2">Picture has been sent!</p>
    <Result bind:resRecieved={$resRecieved} bind:res={$res} />
  {:else}
    <p transition:fade class="font-bold text-4xl p-2">
      You have {$res} thumbs up!
    </p>
  {/if}
</div>
