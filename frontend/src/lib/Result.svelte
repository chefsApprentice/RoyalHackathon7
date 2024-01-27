<script lang="ts">
  export let resRecieved = false;
  export let res = 0;
  import { onMount } from "svelte";

  let getRes = () => {
    resRecieved = true;
  };

  setTimeout(getRes, 2000);
  // if (newLength > curLength) {return}
  res = 0;
</script>
