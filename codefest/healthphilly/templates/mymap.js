var map = L.map('map').setView([51.505, -0.09], 13);

L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={pk.eyJ1Ijoic2phb3VkaTEiLCJhIjoiY2lrdmhnY2J0MDBnN3VnbTNweWh4aDJnZyJ9.wPHcHOABvXHGEM2CsQvZgQ}', {
            attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
            maxZoom: 18,
            id: 'sjaoudi1.p76g9jgk',
            accessToken: 'pk.eyJ1Ijoic2phb3VkaTEiLCJhIjoiY2lrdmhnY2J0MDBnN3VnbTNweWh4aDJnZyJ9.wPHcHOABvXHGEM2CsQvZgQ'
      }).addTo(map);
