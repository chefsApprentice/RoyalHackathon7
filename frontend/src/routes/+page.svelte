<script lang="ts">
    import { onMount } from "svelte";
    import Result from "$lib/Result.svelte";

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
</script>

<div>
    <RedText/>
</div>

<video width={512} bind:this={videoElement}/>
