/************Active Navbar *******************/


$( document ).ready(function() {
  $(function () {
    let activePage = window.location.pathname;
    var currentHash = ""

    console.log(activePage);
    if(activePage.includes("financialHub.php")){
      const navLinks = document.querySelectorAll('.nav-link').
          forEach(link => {
            /*  console.log(link.href);*/

              if (link.href.includes(`Portfolio`)) {
                /*  console.log(`${activePage}`);*/
                  link.classList.add('active');
              }

              else {
                link.classList.remove('active');
              }

          })
    }

    else{
      $(document).scroll(function () {
        $('.anchor').each(function () {
            var top = window.pageYOffset;
            var distance = top - $(this).offset().top;
            var hash = $(this).attr('id');
  
              if (distance < 150 && distance > -530 && currentHash != hash) {
                currentHash = hash;

                const navLinks = document.querySelectorAll('.nav-link').
                forEach(link => {
                  /*  console.log(link.href);*/

                    if (link.href.includes(`${hash}`)) {
                      /*  console.log(`${activePage}`);*/
                        link.classList.add('active');

                    }

                    else {
                      link.classList.remove('active');
                    }

                })

            }
        });
    }); //scroll f(x
    }

  });
});


  
  //Pour Navbar fixe en haut de l'écran quand scroll
  document.addEventListener("DOMContentLoaded", function(){
    window.addEventListener('scroll', function() {
        if (window.scrollY > 0) {
          document.getElementById('navbar_top').classList.add('fixed-top');
          // add padding top to show content behind navbar
          navbar_height = document.querySelector('.navbar').offsetHeight;
          document.body.style.paddingTop = navbar_height + 'px';
        } else {
          document.getElementById('navbar_top').classList.remove('fixed-top');
           // remove padding top from body
          document.body.style.paddingTop = '0';
        } 
    });
  }); 

  function effaceInputs(a_effacer) {
    document.querySelector(a_effacer).reset();
}
        

/* Fait apparaitre ou non formulaire contact*/

// const targetDiv = document.querySelector("#formulaireContact");
// document.addEventListener("DOMContentLoaded", afficheFormulaire);



    //Ssi index.php

    let activePage = window.location.pathname;
    if(!activePage.includes("financialHub.php")){

          /************  Effet tapement clavier ******** */
        class TypeWriter {
          constructor(txtElement, words, wait = 3000) {
            this.txtElement = txtElement;
            this.words = words;
            this.txt = '';
            this.wordIndex = 0;
            this.wait = parseInt(wait, 8);
            this.type();
            this.isDeleting = false;
          }

          type() {
            // Current index of word
            const current = this.wordIndex % this.words.length;
            // Get full text of current word
            const fullTxt = this.words[current];

            // Check if deleting
            if(this.isDeleting) {
              // Remove char
              this.txt = fullTxt.substring(0, this.txt.length - 1);
            } else {
              // Add char
              this.txt = fullTxt.substring(0, this.txt.length + 1);
            }

            // Insert txt into element
            this.txtElement.innerHTML = `<span class="txt">${this.txt}</span>`;

            // Initial Type Speed
            let typeSpeed = 200;

            if(this.isDeleting) {
              typeSpeed /= 2;
            }

            // If word is complete
            if(!this.isDeleting && this.txt === fullTxt) {
              // Make pause at end
              typeSpeed = this.wait;
              // Set delete to true
              this.isDeleting = true;
            } else if(this.isDeleting && this.txt === '') {
              this.isDeleting = false;
              // Move to next word
              this.wordIndex++;
              // Pause before start typing
              typeSpeed = 500;
            }

            setTimeout(() => this.type(), typeSpeed);
          }
        }


        // Init On DOM Load
        document.addEventListener('DOMContentLoaded', init);

        // Init App
        function init() {
          const txtElement = document.querySelector('.txt-type');
          const words = JSON.parse(txtElement.getAttribute('data-words'));
          const wait = txtElement.getAttribute('data-wait');
          
          // Init TypeWriter
          new TypeWriter(txtElement, words, wait);
        }




            
        new svgMap({
          targetElementID: 'svgMap',
          data: {
            data: {

              date: {
                name: 'Année d\'arrivée',
                format: '{0}'
              },
              objetSejour:{
                name:'Motif(s) principal(aux)',
                format:'{0}'
                
              },
              jobs:{
                name:'Principales activitées',
                format:'{0}'
              },
              dureeTotale:{
                name: 'Durée totale du séjour',
                format: '{0}'
              }

            },
            applyData: 'objetSejour',
            values: {
              BR: {date: 1989, objetSejour: "Naissance", dureeTotale:"2 mois" },
              FR: {
                  date: 1990,
                  objetSejour: "Travail / Etudes ",
                  jobs: ["Développeur, Conseiller pédagogique, Professeur particulier",
                        " Commercial"
                  ],
                  dureeTotale:"> 28 ans"
                },
              ES: {date: 2004, objetSejour: "Séjour Linguistique", dureeTotale:"2 semaines"},
              GB: {date: 2006, objetSejour: "Séjour Linguistique", dureeTotale:"3 semaines"},
              IE: {date: 2006, objetSejour: "Tourisme"},
              TR: {date: 2011, objetSejour: "Tourisme"},
              TN: {date: 2002, objetSejour: "Tourisme"},
              MA: {date: 2005, objetSejour: "Tourisme"},
              BE: {date: 2000, objetSejour: "Tourisme"},
              NL: {date: 2000, objetSejour: "Tourisme"},
              PL: {date: 2017, objetSejour: "Tourisme"},
              TH: {date: 2014, objetSejour: "Tourisme"},
              CN: {date: 2016, objetSejour: "Tourisme"},
              KH: {date: 2015, objetSejour: "Tourisme"},
              JP: {
                  date: 2010, objetSejour: "Travail / Séjour Linguistique",
                  jobs: ["Professeur de français",
                        " Bartender, Receptionniste, Assistant de direction (stage), Housekeeper"
                  
                  ],
                  dureeTotale:"2 ans"

            },
              MY: {date: 2018, objetSejour: "Tourisme"},
              KR: {date: 2014, objetSejour: "Tourisme"}
            }
          },
          colorNoData: "#bdbdbd",
          maxZoom: 6
          
          
        });

       
    }

     /* Alertify */

     function enCours(){
      alertify.success().setContent('<h2 id="textAlertify"> Projet en cours... </h2>'); 
    }

    function prochainement(){
      alertify.success().setContent('<h2 id="textAlertify"> Prochainement... </h2>');
    }