<script lang="ts">
  import { fade } from "svelte/transition";

  // Exports var so that main program updates
  export let isDone = false;

  let countDownNum: number | undefined;

  // inits the countdown
  function timer(): null {
    isDone = false;
    if (countDownNum == undefined) countDownNum = 3;
    setTimeout(updateCount, 1000);
    return null;
  }

  // recursive loop for countdown
  let updateCount = () => {
    if (countDownNum! != 0) {
      countDownNum! -= 1;
      setTimeout(updateCount, 1000);
    } else {
      countDownNum = undefined;
      isDone = true;
      return;
    }
  };
</script>

<div>
  <button disabled={countDownNum != undefined} on:click={() => timer()}>
    Start countdown
  </button>

  {#if !Number.isNaN(countDownNum) && countDownNum != undefined}
    <div transition:fade>
      <div
        id="countBubble"
        class="m-10 p-5 bg-gray-300/10 w-min font-bold rounded-xl text-black text-5xl r"
      >
        <p>{countDownNum}</p>
      </div>
    </div>
  {/if}
</div>

<style>
</style>
