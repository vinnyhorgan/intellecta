# Natural Numbers

It's kind of confusing when we try to define numbers, since they are somehow encoded in our brain, they come to us as a spontaneous depiction of the world: two apples, three sheeps, a hundred trees. Usually, the answer includes, explicitly or implicitly, a synonym of the concept of number (like quantity or countability), which we consider a trivial definition since it doesn't really eviscerate the idea of number.

Many mathematicians tried to answer this question, and they came up with different solutions, but they all have something in common.

Everyone agreed on the fact that the idea of number arises from the concept of "emptyness" or "nothingness". If you have nothing, you could have something. That something we call the successor of nothing, the same for the successor of the successor of nothing and so on.

Mathematically speaking, this can be described in multiple ways. The most common one uses a collection of the "nothing object", called the empty set and then creates a collection that contains the empty set. The concept of *twoness* naturally arises since we now have two different collections and, therefore, two different objects. Repeating the process, all the natural numbers can be defined.

The first one to write down a series of Axioms to define the natural numbers was Giuseppe Peano. He said that the natural numbers are a set, he called N, and gave that set these properties:
1. N has a distinguished element which we call ‘0’.
**Simplified:** the set N contains in itself the concept of *emptyness*.

2. There exists a distinguished set [map](maps.md) σ : N → N.
**Simplified:** Applying the map to an element contained in N takes us to another element, which we say is also contained in N.

3. σ is one-to-one.
**Simplified:** the map takes us just to one element. (Return always the same value).

4. There does not exist an element n ∈ N such that σ(n) = 0.
**Simplified:** the map of an element in N never takes us to 0.

Using these axioms, we can see that 0 is mapped to something else, which also is in N. We'll call that "0.next". Now, since 0.next is in N, we can map that to something else, too. We'll call that "0.next.next". This process can continue forever, proving how natural numbers are infinite.

Now we decide to create new symbols for these concepts, and just like that, we perfectly defined the natural numbers {0, 1, 2, 3, 4, ...}

###### ==Curiosity==
The name "zero" literally represents the concept of *emptyness*. In fact, it comes from the latin word *zephirus* which Fibonacci chose to translate the arabic word *sifr* which means both "nothing" and "zero".

==[Video](https://youtu.be/dKtsjQtigag)==

### Sequences

A sequence is an enumerated collection of objects in which repetitions are allowed and order matters. Like a set, it contains members. The number of elements (possibly infinite) is called the length of the sequence. Unlike a set, the same elements can appear multiple times at different positions in a sequence, and unlike a set, the order does matter. Formally, a sequence can be defined as a [function](function) from [natural numbers](natural_numbers) (the positions of elements in the sequence) to the elements at each position.