#lang scheme

;(import (scheme base))

; RSA in Scheme

; Bob key generation

(define p (- (expt 2 13) 1))
(define q (- (expt 2 7) 1))
(define N (* p q))
(define phiN (* (- p 1) (- q 1)))
(define (phif p q) (* (- p 1) (- q 1)))

(define (coprime n m)
  (= (gcd n m) 1))

(define (pubexp phi)
  (let ((e (random phi)))
     (if (and (coprime phi e) (> e 1)) e (pubexp phi))))

; Returns (gcd(a,b) x, y)
; where ax + by = gcd(a, b)
(define (xgcd a b)
  (if (= a 0) (cons b '(0 1))
      (let ((tmp (xgcd (modulo b a) a)))
        (let ((g (first tmp)) (x (second tmp)) (y (third tmp)))
          (append (list g) (list(- y (* (floor (/ b a)) x))) (list x))
        )
      )
  )
)

; Returns (d k)
; The equation e*d + k*phi = 1 has infinite solution
; in the form of d'=(d + phi*n) and k' = (k - e*n)
; n must be greater than (-d)/phi
(define (priexp phi e)
 (let* ((result (xgcd e phi)) (d (second result)) (k (third result)))
   (if (> d 0) (list d k)
       (let ((n (ceiling (/ (* d -1) phi))))
         (list (+ d (* phi n)) (- k (* e n)))
       )
   )
 )
)

(define e (pubexp phiN))
; pk = (e N)
(define pk (list e N))
; sk = (d k)
(define sk (priexp phiN e))


; Alice send message
(define m '220997)

(define (encrypt m pk)
  (modulo (expt m (first pk)) (second pk)))

(define c (encrypt m pk))

; Bob decrypts message

(define (decrypt c sk)
  (let ((d (first sk)))
        (modulo (expt c d) N)))

(display (decrypt c sk))


; Attacco se e piccolo
(define (checkless)
  (if (< (expt m e) N) (expt c (/ 1 e)) #f))

(newline)
(checkless)