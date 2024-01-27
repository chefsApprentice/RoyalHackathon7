<script lang="ts">
    import { onMount } from "svelte";

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
    <p>Royal Hackaway</p>
    <p>Royal Hackaway</p>
    <p>Royal Hackaway</p>
    <p>Royal Hackaway</p>
    <p>Royal Hackaway</p>
    <p>Royal Hackaway</p>
</div>

<video bind:this={videoElement}/>

<style>
    p {
        color: red;
    }
</style>