function walk(num) {
    var lamps = [true];
    lamps = walk_n (num);
    for (var i=0; i<num; i++)
        pass(lamps, i);
    return lamps;
}

function walk_n (num) {
    alamps = new Array(num);
    // primeira ida ao corredor
    for (var i=0; i<num; i++)
        alamps[i] = false;
    return alamps;
}

function pass(lamps, step) {
    for(var i=0; i < lamps.length; i++ /*anda para proxima lampada*/) {
    // se for divisivel pela vez(step) que passa pelo corredor
        if((i+1)%step==0) { 
           lamps[i] = trocalampada(lamps[i]);
       }
     }
    return lamps;
}
function trocalampada(lampada) {
    return !lampada;
}
