<script lang="ts">
    import { onMount } from "svelte";
    import Result from "$lib/Result.svelte";
  import Countdown from "$lib/Countdown.svelte";

    console.log("Royal Hackaway");

    let videoElement: HTMLVideoElement;

    onMount(() => {
        navigator.mediaDevices.getUserMedia({ video: true })
            .then(stream => {
                const video = document.querySelector("video");
                videoElement.srcObject = stream;
                videoElement.onloadedmetadata = () => videoElement.play();
            })
            .catch(err => console.error(err));
    })

    let isDone = false;
</script>
 
<div>
    <Result/>
    <Countdown bind:isDone={isDone} />
</div>

<video width={512} bind:this={videoElement}/>
