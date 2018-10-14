# group-theory-for-cryptography
Piccoli esempi basati su algoritmi studiati nel corso di Algebra per Codici e Crittografia - Unibs

## Algoritmi

- Diffie-Hellman Key Exchange
- El Gamal

## Spiegazione
Gli algoritmi sono basati sul gruppo ciclico (Z_p, .).
Le operazioni di potenza sono realizzate sfruttando la funzione ```pow``` di Python che fornisce anche la possibilità di restituire il risultato ```mod n```.
Il calcolo dell'elemento inverso è realizzato tramite l'algoritmo euclideo esteso.

**NOTA BENE, Il calcolo dell'elemento neutro non è realizzato è fissato ad 1 anche per altri tipi di gruppi**

I numeri casuali sono stati calcolati per mezzo della funzione di libreria ```random.SystemRandom()```, quindi potrebbero non funzionare su alcuni sistemi.
