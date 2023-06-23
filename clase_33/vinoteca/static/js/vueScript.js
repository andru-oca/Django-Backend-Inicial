let sector = {
    template: `
    <section class="cuarto_sector" id="vinoteca" v-if= "value == 'VINOTECA' ">
    <div class="section_data">
        <div>
        <h1>Wines</h1>
        <input type='text' placeholder='ingrese a partir de que rating desea ver' v-model='rating'>
        <button @click="filterData(rating)">Filter Data</button>
        <button @click="fetchDataAxios">Data Axios</button>
        </div>
        <div v-if="error">
            Lo sentimos se produjo un error
            Error: {{nroerror}}
        </div>
        
        <div v-else-if="cargando==false"    class="container">
            <table class="table table-striped">
                <thead>
                    <tr>
                    <th>Id</th>
                    <th>Winery</th>
                    <th>Wine</th>
                    <th>Average</th>
                    <th>Reviews</th>
                    <th>Location</th>
                    <th>Image</th>
                    </tr>
                </thead>
                <tbody v-for="wine of wines">
                    <tr>
                    <td>{{wine.id}}</td>
                    <td>{{wine.winery}}</td>
                    <td>{{wine.wine}}</td>
                    <td>{{wine.rating.average}}</td>
                    <td>{{wine.rating.reviews}}</td>
                    <td>{{wine.location}}</td>
                    <td><img :src="wine.image" :alt="wine.wine"></td>
                    </tr>
                </tbody>
            </table>
        </div>
        <div v-else   class="spinner-border">
            <!-- spinner mientras se esta cargando-->
        </div> 

    </div>

</section>`,

    data: function () {
        return {
            url: "https://api.sampleapis.com/wines/reds",
            wines: [],
            error: false,
            nroerror: 0,
            cargando: true,
            rating: "",
        };
    },
    props: {
        value: String,
    },
    methods: {
        fetchData: function (url) {
            fetch(url)
                .then((response) => response.json())
                .then((data) => {
                    this.wines = data;
                    this.cargando = false;
                })
                .catch((error) => {
                    console.log("error: " + error);
                    this.error = true;
                    this.nroerror = error;
                });
        },

        filterData: function (rating) {
            console.log(rating);
            this.wines = this.wines.filter((e) => e.rating.average > rating);
        },
        async fetchDataAxios() {
            let res = await axios(this.url);
            console.log(res.data);
        },
    },
    created() {
        this.fetchData(this.url);
    },
};

let app = {
    data: function () {
        return {
            lista: ["INICIO", "CONTACTO", "HABILIDADES"],
            habilidades: [
                "SQL",
                "PYTHON",
                "REACT",
                "VUE",
                "GITHUB-GIT",
                "POWER BI",
                "DJANGO",
            ],
            intro: "Mi nombre es Anderson, soy docente , programador y analista de datos",
            value: null,
        };
    },
    methods: {
        clickedShow($event) {
            this.value = $event.target.innerHTML;
        },
    },

    components: {
        "sector-component": sector,
    },
    delimiters: ["--", "--"],
};

let appRoot = Vue.createApp(app).mount("#app");
