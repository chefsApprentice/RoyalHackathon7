<script lang="ts">
  import { fade } from "svelte/transition";

  // Exports var so that main program updates
  export let isDone = false;

  let countDownNum: number | undefined;

  // inits the countdown
  function timer(): null {
    isDone = false;
    if (countDownNum == undefined) countDownNum = 4;
    setTimeout(updateCount, 1000);
    return null;
  }

  // recursive loop for countdown
  let updateCount = () => {
    if (countDownNum! > 1) {
      countDownNum! -= 1;
      setTimeout(updateCount, 1000);
    } else {
      countDownNum = undefined;
      isDone = true;
      return;
    }
  };
</script>

<div class="mb-5">
  <button disabled={countDownNum != undefined} on:click={() => timer()}>
    Start countdown
  </button>

  {#if !Number.isNaN(countDownNum) && countDownNum != undefined && countDownNum != 4}
    <div transition:fade class="grid h-3/4 place-items-center absolute">
      <div
        id="countBubble"
        class="m-10 p-5 bg-gray-100/10 w-max h-max font-bold rounded-xl text-black text-5xl z-50"
      >
        <p>{countDownNum}</p>
      </div>
    </div>
  {/if}
</div>

<style>
</style>
