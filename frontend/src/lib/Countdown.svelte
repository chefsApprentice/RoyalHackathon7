<script lang="ts">
  export let isDone = false;

  let countDownNum: number | undefined;

  function timer(): null {
    isDone = false;
    if (countDownNum == undefined) countDownNum = 3;
    setTimeout(updateCount, 1000);
    return null;
  }

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
  <button on:click={() => timer()} class="bg-green-300">
    Start countdown
  </button>

  {#if !Number.isNaN(countDownNum) && countDownNum != undefined}
    <div
      id="countBubble"
      class="m-10 p-5 bg-gray-300 w-min font-bold rounded-full text-white text-lg"
    >
      <p>{countDownNum}</p>
    </div>
  {/if}
</div>

<style>
</style>
