<script lang="ts">
    export let isDone = false; 
        
    let countDownNum: number | undefined ;
   
    function timer () : null{
        setInterval(updateCount, 1000);
        return null;
    }

    let updateCount = () => {

        if (countDownNum == undefined) countDownNum = 4;

        if (countDownNum! == 0) {
            isDone = true;
            countDownNum = undefined;
        } else if (countDownNum != undefined) {
            countDownNum -= 1;
        }

    
    }

</script>

<div>
    <button on:click={timer()}>
        Start countdown 
    </button>

    <p style = {(countDownNum == undefined  || countDownNum > 4 ? "visibility:hidden" : "visibility:visible")}>
        {countDownNum}
    </p>
</div>

<style>

</style>