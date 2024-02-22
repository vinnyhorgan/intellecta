# Natural Numbers & Sequences

### Natural numbers

It's kind of confusing when we try to define numbers, since they are somehow encoded in our brain, they come to us as a spontaneous depiction of the world: two apples, three sheep, a hundred trees. Usually, the answer includes, explicitly or implicitly, a synonym of the concept of number (like quantity or countability), which we consider a **trivial definition** since it doesn't really eviscerate the idea of number.

This type of questions often, if not always, fall into **philosophic debacles**. The most common and accepted solutions are based on the construction of an **axiomatic system**. That is, a set of primitive notions blindly accepted as true, upon which logical deductions and theorems can be defined.

Multiple set of axioms has been proposed, but usually the idea of natural numbers arises from the concept of "emptiness" or "nothingness". If you have nothing, you could have something. That something we call the successor of nothing, the same for the successor of the successor of nothing and so on.

The most used axioms were stated by Giuseppe Peano. Even if nowadays they are known to be paradoxical and can lead to contradictions, the **Peano axioms** are still incredibly useful and relevant, other than a strong foundation of mathematics. 

He claimed the natural numbers are the members of a [set](sets_maps.html) \(\N\), and gave that set these properties:
>1. ##### \(\N\) has a distinguished element which we call ‘0’.

**Simplified:** The set \(\N\) contains in itself the concept of *emptiness*.

> 2. ##### There exists a distinguished set [map](sets_maps.html) \(\sigma : \N \to \N \).

**Simplified:** There is a map that applied to an element contained in \(\N\) takes us to another element, which is also contained in \(\N\).

> 3. ##### \(\sigma\) is one-to-one.

**Simplified:** The map always returns only one specific value, and two elements cannot be mapped to the same value.

> 4. ##### There does not exist an element \(n \in \N \) such that \(\sigma (n) = 0\).

**Simplified:** The map of an element in \(\N\) never takes us to 0.

The fifth axiom is the most complex, it is called the induction axiom, and it formalizes what could seems a trivial logical assumption.

> 5. ##### If \(\phi\) is a unary predicate such that:
 > - \(\phi (0)\) is true, and
 > - for every natural number \(n\), \(\phi (n)\) being true implies that \(\phi (\sigma (n))\) is true,
 >then \(\phi (n)\) is true for every natural number \(n\).

**Simplified:** If a certain statement is proved to be true for both a random number \(n \in \N \) and for \(\sigma (n) \in \N\) and it is true for the number '0', then is reasonable to be true for every single \(n \in \N\). This can be visualized as a **domino effect**, in that case it would state: if for every piece that falls the next one falls too and the first one falls, then it is reasonable to assume that every piece in the line will fall. 

Let's call the map \(\sigma \) "the successor". Notice that the successor of 0 is mapped to something else, which is also in \(\N\). We'll call that "0.next". Now, since 0.next is in \(\N\), it's successor is in \(\N\), too. We'll call that "0.next.next". Now we decide to create new symbols representing these concepts that arise from recursively applying the successor: \(\{0, 1, 2, 3, 4, ...\}\).

Since we cannot check infinite terms we use the axiom of induction, paired with the others, to prove that all natural numbers are obtained using the successor map:

> It is true that 0 is in \(\N\). _First axiom._
> 
> It is also true that for every \(n \in \N, \sigma (n) \in \N \). _Second to fourth axioms._
> 
> Then it is true that every natural number \(\n\) is in \(\N\). _Fifth axiom._

Finally, we arrived at the definition of natural numbers as we know them. From now on, when we will refer to them, you will not only know the spontaneous and trivial definition, but you'll be able to formally describe them.

---
**Curiosity**
The name "zero" literally represents the concept of *emptiness*. In fact, it comes from the latin word *zephirus* which Fibonacci chose to translate the arabic word *sifr* which means both "nothing" and "zero".
---
### Sequences

A sequence is an enumerated collection of objects in which repetitions are allowed and order matters. Like a set, it contains members. The number of elements is called the length of the sequence. Unlike a set, the same elements can appear multiple times at different positions in a sequence, and unlike a set, the order does matter. Formally, a sequence can be defined as a [function](sets_maps.html) from [natural numbers](natural_numbers_sequences.html) (the positions of elements in the sequence) to the elements at each position.

------
Other resources:
- [What IS a number? Explained as a mathematician](https://youtu.be/dKtsjQtigag)