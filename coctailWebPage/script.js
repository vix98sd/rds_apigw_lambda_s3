function getAllCoctails(){
    $.getJSON('https://b393ka3x98.execute-api.us-east-1.amazonaws.com/v1/coctails/', function(data) {
        data.forEach(coctail => {
            $("#coctailContainer").append(`
            <div class="col-sm-4 d-flex align-items-stretch my-3">
                <div class="card">
                    <img src="${coctail[5]}" class="card-img-top" alt="coctail_${coctail[1]}">
                    <div class="card-body">
                      <h5 class="card-title">${coctail[1]}</h5>
                      <p class="card-text">${coctail[6]}</p>
                      <p class="card-text">${coctail[7]}</p>
                      <button type="button" class="btn btn-primary" onClick="save_and_open(${coctail[0]})">Learn more</button>
                    </div>
                  </div>
            </div>
            `);
        });
    });
}

function open_coctail_details(){
    window.open("coctail_details.html", "_self");  
}

function getCoctailById(coctailId) {
    $.getJSON('https://b393ka3x98.execute-api.us-east-1.amazonaws.com/v1/coctails/' + coctailId, function(data) {
        var ingredients = data.ingredients.split(";");
        var measures = data.measures.split(";");
        console.log(data);
        $("#coctailContainer").append(`
        <div class="card mb-3"">
            <div class="row g-0">
                <div class="col-md-5 d-flex">
                <img src="${data.imageUrl}" class="card-img" alt="coctail_${data.coctailName}">
                </div>
                <div class="col-md-7">
                <div class="card-body">
                    <h5 class="card-title">${data.coctailName}</h5>
                    
                    <hr>

                    <dl class="row">
                        <dt class="col-sm-3">Category</dt>
                        <dd class="col-sm-9">${data.category}</dd>
                        <dt class="col-sm-3">Type</dt>
                        <dd class="col-sm-9">${data.type}</dd>
                        <dt class="col-sm-3">Glass</dt>
                        <dd class="col-sm-9">${data.glass}</dd>
                    </dl>

                    <hr>

                    <dl class="row" id="measures">
                        <dt class="col-sm-3">Ingredient:</dt>
                        <dd class="col-sm-9">Measure:</dd>
                    </dl>

                    <hr>

                    <h5>Instructions:</h3>
                    <p class="card-text">${data.instructions}</p>
                    
                    <p class="card-text"><small class="text-muted">Last updated ${Math.floor((Math.random() * 50) + 2)} mins ago</small></p>
                </div>
                </div>
            </div>
        </div>
        `);

        for (let i = 0; i < ingredients.length; i++) {    
            $("#measures").append(`
                <dt class="col-sm-3">${ingredients[i]}</dt>
                <dd class="col-sm-9">${measures[i]}</dd>
            `);
        }
    });
}

    