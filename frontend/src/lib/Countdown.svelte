<script lang="ts">
    export let isDone = false; 
        
    let countDownNum: number | undefined ;
   
    function timer () : null{
        isDone = false;
        if (countDownNum == undefined ) countDownNum = 3;
        setTimeout(updateCount, 1000);
        return null;
    }

    let updateCount = () => {
        if (countDownNum! != 0) { countDownNum! -= 1;  
        setTimeout(updateCount, 1000);  }
        else { countDownNum = undefined; isDone = true; return;}
    }

</script>

<div>
    <button on:click={() => timer()}>
        Start countdown 
    </button>

    <div id = "countBubble"  class=" p-5; bg-green-300;">
        {#if !Number.isNaN(countDownNum) && countDownNum != undefined}
            <p> {countDownNum} </p>
        {/if}
       
    </div>

</div>

<style>
    #countBubble {

    }
</style>