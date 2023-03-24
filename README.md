# Interactive Quadtree

A point quadtree is a data structure used to store and efficiently search for points in a two-dimensional space. It is a hierarchical tree structure where each node represents a square region in the space, and points are stored at the leaf nodes of the tree.

Each node in the tree has four children, corresponding to the four quadrants of the square region represented by the node. The tree is built recursively by subdividing each square region into four smaller squares until each leaf node contains at most one point.

To search for a point in the quadtree, the search starts at the root node and recursively descends the tree, choosing the appropriate child node at each level based on the quadrant in which the search point lies. The search terminates when a leaf node containing the point is reached or when an empty node is encountered.

Point quadtree is commonly used in various applications such as geographic information systems, computer graphics, and computer vision. It provides an efficient way to search for nearest neighbors, range search, and spatial indexing.

<div align="center">
<img width=800 src="media/quadtree.png"/>  
</div>
