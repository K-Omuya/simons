// Function to fetch data from APIs and populate the table
async function fetchPrices(product) {
    const apiUrls = [
        `https://example.com/api/jumia?product=${product}`,
        `https://example.com/api/kilimall?product=${product}`,
        `https://example.com/api/copia?product=${product}`
    ];

    const tableBody = document.querySelector('#price-table tbody');
    tableBody.innerHTML = ''; // Clear previous results

    for (const url of apiUrls) {
        try {
            const response = await fetch(url);
            if (!response.ok) throw new Error('Failed to fetch data');
            const data = await response.json();

            data.forEach(item => {
                const row = `
                    <tr>
                        <td>${item.productName}</td>
                        <td>${item.platform}</td>
                        <td>${item.price}</td>
                        <td><a href="${item.link}" target="_blank">View</a></td>
                    </tr>
                `;
                tableBody.innerHTML += row;
            });
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    }
}

// Event listener for search button
document.getElementById('search-button').addEventListener('click', () => {
    const searchTerm = document.getElementById('search-input').value.trim();
    if (searchTerm) {
        fetchPrices(searchTerm);
    } else {
        alert('Please enter a product name.');
    }
});
