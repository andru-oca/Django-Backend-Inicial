/*Una forma de hacer algo interactivo basandonos en un principio de SPA*/

let nodeLinks = document.querySelectorAll('#header a');

let links = Array.from(nodeLinks)

links.forEach(e => {
    
    let item = e.innerHTML.toLocaleLowerCase().trim();
    document.getElementById(`${item}`).classList.add('noShow');

})


nodeLinks.forEach(
    e => e.addEventListener(
        'click',
        (e)=>{
            let toShow= e.target.innerHTML.toLowerCase().trim();
            document.getElementById(`${toShow}`).classList.toggle('noShow');

        }
    )
)




