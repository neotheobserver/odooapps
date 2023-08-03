document.addEventListener("input", (event) => {
    if (event.target.type === "text" && event.target.id.indexOf("date") === -1 && event.target.className.indexOf("o_datepicker_input") === -1){
       var text = event.target.value;
       var convert = setUnicodePreeti(text);
       event.target.value = convert;
       return true;
    }
});