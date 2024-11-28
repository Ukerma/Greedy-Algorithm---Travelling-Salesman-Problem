<h1>📍 Profitable Route Planner</h1>
<p>
   This project calculates and visualizes the most profitable and least profitable delivery routes for a given set of cities. It considers distances, delivery income, and fuel costs to determine the best routes. The project is implemented in Python and uses algorithms to maximize or minimize profit for the delivery operation.
</p>

<h2>🛠️ Features</h2>
<ul>
   <li> Generate random city positions and assign random delivery demands.</li>
   <li> Create a distance matrix for calculating distances between cities.</li>
   <li> Use a greedy algorithm to calculate the most profitable and least profitable routes.</li>
   <li> Calculate total profit, distance, revenue, and fuel costs for each route.</li>
   <li> Visualize routes using <code>NetworkX</code> and <code>Matplotlib</code>.</li>
</ul>

<h2>⚙️ Technologies Used</h2>
<ul>
   <li> <strong>Language:</strong> Python</li>
   <li> <strong>Libraries:</strong> 
      <ul>
         <li><code>numpy</code>: For mathematical calculations.</li>
         <li><code>random</code>: For generating random positions and demands.</li>
         <li><code>matplotlib</code>: For visualizing routes.</li>
         <li><code>networkx</code>: For creating graph-based route visualizations.</li>
      </ul>
   </li>
</ul>

<h2>🚀 How to Use</h2>
<ol>
   <li> Clone or download the repository to your local machine.</li>
   <li> Ensure the required Python libraries are installed:
      <pre><code>pip install numpy matplotlib networkx</code></pre>
   </li>
   <li> Run the script using any Python IDE or terminal.</li>
   <li> Observe the printed results in the console and the visualized routes for both the most and least profitable routes.</li>
</ol>

<h2>💡 Example Output</h2>
<pre>
Most profitable route: ['A', 'B', 'C', ..., 'A']
Route distance: 456
Revenue: 1250
Fuel cost: 500
Net profit: 750

Least profitable route: ['A', 'D', 'E', ..., 'A']
Route distance: 789
Revenue: 980
Fuel cost: 600
Net profit: 380

Unit price of the product: 599
</pre>
<p>Route visualizations will also be displayed using graphs.</p>

<h2>👨‍💻 Author</h2>
<p>
   This project was developed by <strong>Umut Kerim ACAR (ukerma)</strong> and <strong>Tuna DURUKAN (Ranewen)</strong>.
</p>
