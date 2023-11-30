const converter = (d) =>
    [
        0 | d,
        "° ",
        0 | (((d = (d < 0 ? -d : d) + 1e-4) % 1) * 60),
        "' ",
        0 | (((d * 60) % 1) * 60),
        '"',
    ].join("");

const getCoordinates = async () => {
    let coord = `N 49° 16' 35.173" / W 0° 42' 11.30"`;

    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function (position) {
            const latitude = position.coords.latitude;
            const longitude = position.coords.longitude;

            coord = `Latitude: ${converter(latitude)}, Longitude: ${converter(
                longitude
            )}`;

            document.querySelector(".coords").innerHTML = coord;
        });
    } else {
        document.querySelector(".coords").innerHTML = coord;
    }
};

getCoordinates();
