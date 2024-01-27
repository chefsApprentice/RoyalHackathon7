<script lang="ts">
  import { onMount } from "svelte";
  // import Result from "$lib/Result.svelte";
  import Countdown from "$lib/Countdown.svelte";
  import { writable } from "svelte/store";
  import { fade } from "svelte/transition";

  console.log("Royal Hackaway");

  let videoElement: HTMLVideoElement;
  let canvasElement: HTMLCanvasElement;
  // let photoElement: HTMLImageElement;

  let sendData = async (data: string) => {
    let formData = new FormData();
    formData.append("image", data);

    // posts the data and creates that req as a var
    let response = await fetch("http://localhost:3000/img/", {
      method: "POST",
      mode: "cors",
      cache: "no-cache",
      credentials: "same-origin",
      headers: {
        "Content-Type": "application/json",
      },
      redirect: "follow",
      referrer: "no-referrer",
      body: JSON.stringify({
        image: data,
      }),
    });
    // var that qaits the req's response
    let dataRecieved = await response.json();

    // Checks recieved data, updates data to match
    if (dataRecieved != undefined) {
      resRecieved = writable(true);
      console.log(dataRecieved);
      // let dataRecieved = JSON.stringify(success.body);
      res.set(dataRecieved);
    }
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

    resRecieved.subscribe((recieved) => {
      // TODO: Change the background colour based on the result
      // Right now the output json isn't final
      if (!recieved) return;

      const body = document.body;
      let sway = 1;
      switch (sway) {
        case -1: // Majority Dislike
          body.style.backgroundColor = "#ffd9d9";
          break;
        default:
        case 0: // Equal
          break;
        case 1: // Majority Like
          body.style.backgroundColor = "#cdffcd";
          break;
      }
    });
  });

  // Defines res (the thumbs up score)
  let res = writable({ up: 0, down: 0 });
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
    // console.log("data:" + data);
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
  <div class="flex flex-col w-full mb-5 items-center justify-center">
    <h1>Mass Polling System</h1>
    <p>Get a group and put your thumbs up and down to vote!</p>
  </div>

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
  {:else if $resRecieved === false}
    <p transition:fade class="font-bold text-4xl p-2">Picture has been sent!</p>
    <!-- <Result bind:resRecieved={$resRecieved} bind:res={$res} /> -->
  {:else}
    {#await $res}
      <p class="animate-pulse">Predicting...</p>
    {:then response}
      <div transition:fade class="flex font-bold text-3xl py-2">
        <span>I see</span>
        <div class="bg-black/5 rounded px-1 pb-1 mx-2">
          <span class="text-green-600">{response.up}👍</span>
        </div>
        <span>and</span>
        <div class="bg-black/5 rounded px-1 pb-1 mx-2">
          <span class="text-red-400">{response.down}👎</span>
        </div>
        <span>!</span>
      </div>
    {:catch error}
      <p>Something went wrong!</p>
    {/await}
  {/if}
</div>
