# Sets & Maps

### Sets

 The philosophical idea behind the construction of a collection is really straightforward: not everything is itself, and *something* has to be *something else*. This means that since distinct things exist, they can be collected, and therefore, we can construct a collection. A set is then defined to be a mathematical model for a **well-defined collection of distinct things**.

This idea is so commonly accepted, that even if everyone used it for thousands of years, no-one thought to described it in the first place. In fact, the study of sets began only 'recently', when someone got interested in studying sets with infinite things in them[^1].

Bernard Bolzano was chronologically the first. Then, Bernard Riemann proposed the study of sets as the basis of the study of shapes. Finally, Richard Dedekind introduced the idea of set as a new mathematical object.

Surely something was in the air, and the formalization of such a fundamental concept was about to come.

**Georg Cantor** first described the set as "the understanding of a collection as a whole made of definite and separate objects of our thought." He then called "elements" the objects contained in sets, and philosophically defined the properties of sets:

> ##### Union

"The uniting of many sets $A,B,C,...$ into a single set $M$, is the collection of the elements of $A,B,C,...$"
In modern notation: $$A \cup B = \{x \in A | x \notin B\}$$
**Read:** $A$ union $B$ is equal to the set of all "$x$"s in $A$ such that "$x$" is not in $B$.

![union](https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Venn0111.svg/2560px-Venn0111.svg.png)

> ##### Subset

"We will call by the name subset of a set $M$ any other set $A$ whose elements are also elements of $M$."
In modern notation: $$\forall x \in A, x \in M \longrightarrow  A \subset M$$
**Read:** if for all "$x$"s in $A$, "$x$" is also in $M$, then $A$ is a subset of $M$.

![subset](https://upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Venn_A_subset_B.svg/1920px-Venn_A_subset_B.svg.png)

> ##### Intersection

The **intersection** of two sets A and B, denoted by $A \cap B$, is the set containing all elements of A that also belong to B.

![intersection](https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Venn0001.svg/2560px-Venn0001.svg.png)

>##### Complement

The complement of a set A with respect to a set M, also termed the **set difference** of M and A, written A \\ M is the set of elements in M that are not in A.
$$M \setminus A = \{x \in M | x \notin A\}$$

![complement](https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Venn10.svg/1920px-Venn10.svg.png)

>##### Cardinality

Cantor describes the cardinality as "a concept arising from a set M when we make a double abstraction of its elements. First, we abstract every element of the set from his nature (his characteristics), so that they become indistinguishable *units*. Then, we abstract the set from the concept of *order* in which such *units* are given."

In simpler terms, the cardinality of a set represents the concept of *quantity* that arises from the elements within the set.


[^1] the concepts of infinity and infinite sets are well explained in ["Infinity & Infinitesimal"](infinity_infinitesimal.html).

### Maps

A map is a fundamental concept that describes a relationship between two sets. More formally, a map $\sigma$ from a set X to a set Y, denoted as $\sigma :X\to Y$ , assigns to some element x in X one or more elements y in Y.

Consider a simple example: suppose we have two sets, X={1,2,3} and Y={a,b,c}. A map f from X to Y could be defined such that $\sigma (1)=a$, $\sigma(2)=b$, and $\sigma (3)=c$. This illustrates how each element in X is uniquely associated with an element in Y through the map $\sigma$.

Mathematical maps can be categorized in various types, each with its own properties and characteristics. Some common types of maps include:

1. **Injective (One-to-One) Maps**: A map is injective if each element in the domain is mapped to a distinct element in the codomain. In other words, no two distinct elements in the domain are mapped to the same element in the codomain.
    
2. **Surjective (Onto) Maps**: A map is surjective if every element in the codomain has at least one pre-image in the domain. In simpler terms, the map covers the entire codomain.
    
3. **Bijective Maps**: A map is bijective if it is both injective and surjective. Bijective maps establish a one-to-one correspondence between elements in the domain and codomain, meaning each element in one set corresponds to exactly one element in the other set.


Now that we have a clear understanding of maps, it is possible to formally define the cardinality of a set.

In fact, Cantor says that two sets A and B are equivalent "if it is possible to put them in such a
relation to one another that to every element of each one of them corresponds one and only one element."