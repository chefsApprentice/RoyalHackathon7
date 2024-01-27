<script lang="ts">
import { onMount } from "svelte";

  let tableData = [];

  onMount(async () => {
    const res = await fetch(`https://jsonplaceholder.typicode.com/posts`);
    tableData = await res.json();
    console.log(tableData);
  });

</script>



<div>
    <p> </p>
</div>

<style>
    p {
        color: red;
    }
</style>