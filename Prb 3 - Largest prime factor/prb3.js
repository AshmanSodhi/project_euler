function larg_primt(n){
    i = 2
    while (i*i <= n){
        if (n%i){
            i = i + 1 ;
        }

        else {
            n = Math.floor(n/i);
        }
    }

    console.log(n);

}

larg_primt(600851475143)