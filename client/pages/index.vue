<template>                 <!-- změnit img v tutorial_img_box na text, tak aby v něm šlo scrollovat-->
    <div>                  <!-- zde mám CSS a obrátky v /assets v tutoriálu to bude v /static (/assets tam nebude) -->
        <div class="div1">
                <!-- horní menu -->
        </div>
        <div class="site_body">
            <div class="text_color links">
                <!-- odkazy (kotva) -->
                <a class="link_t_h2" href="#" @click="scrollToSection('django-id')"> Django </a> <br>
                    <a class="link_t_h3" href="#" @click="scrollToSection('django-install-id')"> Instalace </a>  <br>
                    <a class="link_t_h3" href="#" @click="scrollToSection('django-project-id')"> Vytvoření projektu </a>  <br>
                    <a class="link_t_h3" href="#" @click="scrollToSection('django-library-id')"> Stažení knihoven </a>  <br>
                    <a class="link_t_h3" href="#" @click="scrollToSection('django-settings-id')"> Nastavení </a>  <br>
                <a class="link_t_h2" href="#" @click="scrollToSection('nuxt-id')"> Nuxt </a> <br>
                    <a class="link_t_h3" href="#" @click="scrollToSection('nuxt-install-id')"> Instalace </a>  <br>
                    <a class="link_t_h3" href="#" @click="scrollToSection('nuxt-project-id')"> Nový projekt </a>  <br>
                    <a class="link_t_h3" href="#" @click="scrollToSection('nuxt-layout-id')"> Rozložení </a>  <br>
                    <a class="link_t_h3" href="#" @click="scrollToSection('nuxt-settings-id')"> Nastevení </a>  <br>
                <a class="link_t_h2" href="#" @click="scrollToSection('pages-id')"> Stránky </a> <br>
                <a class="link_t_h3" href="#" @click="scrollToSection('pages-layout-id')"> Layout </a>  <br>
                    <a class="link_t_h3" href="#" @click="scrollToSection('pages-recipes-id')"> Recepty </a>  <br>
                    <a class="link_t_h3" href="#" @click="scrollToSection('pages-register-id')"> Registrace </a> <br>
                    <a class="link_t_h3" href="#" @click="scrollToSection('pages-login-id')"> Přihlášení </a>   
            </div>
            <div class="content">
                <h1 class="text_color"> AJAX tutoriál </h1>
                    <p class="text_color normal_text">
                        Toto je tutoriál pro tvorbu webových aplikací, které využívají framework django pro backend 
                        a framework nuxt pro frontend. Zdrojový kód celé stránky je k nalezení 
                        <a href="https://github.com/pallmis/dlouhodobka" target="_blank" class="page_link"> zde </a>
                    </p>
                <h2 class="text_color title_text" id="django-id"> Django </h2>  <!--úvod -->
                        <p class="text_color normal_text">      
                            Django je oblíbemý python framework využívanž pro tvorbu webu. V tomto tutoriálu bude využit k 
                            tvorbě backendu, což je jeho primární využití. Bude zde nastavení djanga, komunikace djanga s 
                            frontendem, vytváření databáze, vytváření rout a práce s knihovny framework a corsheaders.
                        </p>
                    <h3 class="text_color title_text" id="django-install-id"> Instalace Djanga </h3>
                        <p class="text_color normal_text">   
                            Django můžeme stáhnout buď přímo príkazem "pip install django" anebo virtuálně přímo pro 
                            tento projekt, tak že si stáhneme pipenv příkazem "pip install pipenv" a ve složce, ve které
                            chceme mít náš projekt aktivujeme virtuální prostředí příkazem "pipenv shell" a nainstalujeme 
                            django příkazem "pipenv install django"
                        </p>
                        <div class="tutorial_img_box">
                            <p class="text_color tutorial_box_title"> konzole </p>
                            <img src="~/assets/img/django_install.png" class="tutorial_img">    
                        </div>
                    <h3 class="text_color title_text" id="django-project-id"> Vytvoření Django projektu </h3>  <!-- vytvoření projektu -->
                        <p class="text_color normal_text">  
                            Je potřeba otevřít konzoli a vytvořit nový projekt pomocí příkazu  
                            "django-admin startproject vasprojekt", vznikne složka, která by měla vypadat takto:
                        </p>
                        <div class="tutorial_img_box"> 
                            <p class="text_color tutorial_box_title"> nový projekt </p>  
                            <img src="~/assets/img/novy_projekt.png" class="tutorial_img">
                        </div>
                            <p class="text_color normal_text">  
                            Poté je potřeba vytvořit jednotlivou aplikaci. První se v konzoli musíme přesunout do 
                            nově vytvořené složky našeho projektu příkazem "cd vasprojekt" a v ní vytvořit novou 
                            aplikaci příkazem "python manage.py startapp vaseaplikace". Výsledek by měl vypadat takto:
                        </p>
                        <div class="tutorial_img_box">
                            <p class="text_color tutorial_box_title"> nová aplikace </p>
                            <img src="~/assets/img/novy_projekt2.png" class="tutorial_img">
                        </div>
                    <h3 class="text_color title_text" id="django-library-id"> Stažení knihoven </h3>  <!-- používané knihovny -->
                        <p class="text_color normal_text">   <!-- zde dopsat knihovny pokud přibudou --> 
                            V tomto tutoriálu se budou používat knihovny: rest framework, corsheaders. Ty si stáhnete
                            pomocí příkazů "pip install django-rest-framework" a "pip install django-cors-headers" nebo 
                            pokud jste si vybrali virtuální instalaci, tak pomocí "pipenv install django-rest-framework" 
                            a "pipenv install django-cors-headers". U virtuální instalace používáme konzoli otevřenou přes
                            příkaz "pipenv shell"  
                        </p>
                        <div class="tutorial_img_box">
                            <p class="text_color tutorial_box_title"> konzole </p>
                            <img src="~/assets/img/stazeni_knihoven.png" class="tutorial_img">  
                        </div>
                    <h3 class="text_color title_text" id="django-settings-id"> Nastavení djanga </h3>  <!-- nastavení -->
                    <h4 class="text_color title_text"> Nastavení projektu </h4>
                        <p class="text_color normal_text">      <!-- INSTALLED_APPS -->
                            První provedeme všechno potřebné nastavení našeho projektu
                            v souboru settings.py. si jako první zaregistrujeme všechny stáhnuté knihovny, spolu se všemi 
                            námi vytvořenými aplikacemi, tak že je přidáme do seznamu INSTALLED_APPS. Dále můžeme smazat sessions 
                            ze seznamu použitých aplikací, jelikož zde budeme použávat tokeny. takto by pak měl vypadat seznam INSTALLED_APPS: 
                        </p>
                        <div class="tutorial_img_box">
                            <p class="text_color tutorial_box_title"> .../vasprojekt/settings.py </p>
                            <img src="~/assets/img/installed_apps.png" class="tutorial_img">
                        </div>
                        <p class="text_color normal_text">      <!-- MIDDLEWARE -->
                            Dále přidáme corsheaders middleware do našich použývaných middleware tak že do seznamu 
                            MIDDLEWARE přidáme: 'corsheaders.middleware.CorsMiddleware', je vhodné mít corsheaders middleware 
                            v seznamu na začátku před middleware moduly djanga, jinak mohou nastat problémy.
                            takto by pak měl vypadat seznam MIDDLEWARE: 
                        </p>
                        <div class="tutorial_img_box">
                            <p class="text_color tutorial_box_title"> .../vasprojekt/settings.py </p>
                            <img src="~/assets/img/middleware.png" class="tutorial_img">   
                        </div>
                        <p class="text_color normal_text">
                            Jako další si do seznamu CORS_ALLOWED_ORIGINS, což jsou povolené URL adresy, přidáme adresu našeho
                            frontendu, v tomto tutoriálu to bude "http://localhost:3000".
                            Poté nastavíme ROOT_URLCONF na "vaseaplikace.urls".
                        </p>
                        <div class="tutorial_img_box">
                            <p class="text_color tutorial_box_title"> .../vasprojekt/settings.py </p>
                            <img src="~/assets/img/settings_3.png" class="tutorial_img">     
                        </div>
                        <p class="text_color normal_text">
                            Dále sei nastavíme potřebné routy v urls.py našeho projektu podle obrázku:
                        </p>
                        <div class="tutorial_img_box">
                            <p class="text_color tutorial_box_title"> .../vasprojekt/urls.py </p>
                            <img src="~/assets/img/urls.png" class="tutorial_img">     
                        </div>
                    <h4 class="text_color title_text"> Nastavení aplikace </h4>
                    <h5 class="text_color title_text"> Vytvoření rout </h5>
                        <p class="text_color normal_text">
                            V tomto kroku je vytvoření potřebných rout backendu. Tyto routy definují URL adresy,
                            na které bude frontend posílat requesty a tyto adresy spojují s funkcemi, které tyto
                            requesty vyhodnocují.
                        </p>
                        <div class="tutorial_img_box">
                            <p class="text_color tutorial_box_title"> .../vaseaplikace/urls.py </p>
                            <img src="" class="tutorial_img">    
                        </div>
                    <h5 class="text_color title_text"> Vytvoření databáze </h5>
                        <p class="text_color normal_text">
                            V djangu se databáze vytváří a edituje pomocí souboru models.py. V tomto souboru si zadefinujeme
                            jak budou vypadat tabulky naší databáze a relace mezi nimi. Django poté aplikaci vytvoří pomocí 
                            migrací, které vytvoříme příkazem "python manage.py makemigrations" v konzoli otevřené v našem projektu.
                            Tyto migrace aplikujeme příkazem "python manage.py migrate". Pokud by jsme chtěly smazat omylem vytvořené 
                            migrace, všechny vytvořené migrace najdeme ve ".../vašeaplikace/migrations", jejich název začíná 4-mi čísly.
                            Pro aplikaci, kterou vytváříme budeme potřebovat tabulku s recepty, uživately a tagy. Ty vytvoříme
                            podle následujícího kódu:
                        </p>
                        <div class="tutorial_img_box">
                            <p class="text_color tutorial_box_title"> .../vaseaplikace/models.py </p>
                            <img src="~/assets/img/models.png" class="tutorial_img">    
                        </div>


                <h2 class="text_color title_text" id="nuxt-id"> Nuxt</h2>
                        <p class="text_color normal_text">
                            Nuxt je framework postavený na Vue.js, který je používaný pro tvorbu frontend webu.
                        </p>
                    <h3 class="text_color title_text" id="nuxt-install-id"> Instalace požadavků </h3>
                        <p class="text_color normal_text">
                            Nuxt pro své fungování vyžaduje knihovnu Node.js, kterou můžete stáhnout 
                            <a href="https://nodejs.org/en/download" target="_blank" class="page_link">zde</a>. Nuxt 
                            ve své dokumentaci doporučuje verze začínající čísly 16 nebo 14.
                        </p>
                    <h3 class="text_color title_text" id="nuxt-project-id"> Vytvoření Nuxt projektu </h3>
                        <p class="text_color normal_text">
                            Jakmile máte Node.js, tak můžete vytvořit nový projekt pomocí příkazu "npm init nuxt-app vasclient"
                            Tento příkaz se vás zeptá na nějaké parametry, takto vypadají volby pro tento tutoriál:
                        </p>
                        <div class="tutorial_img_box">
                            <p class="text_color tutorial_box_title"> konzole </p>
                            <img src="" class="tutorial_img"> <!-- přidat obrázek -->    
                        </div>
                    <h3 class="text_color title_text" id="nuxt-layout-id"> Rozložení Nuxtu </h3>
                        <p class="text_color normal_text">
                            Po vytvoření projektu, by vám měla vzniknout složka, která vypadá takto:
                        </p>
                        <div class="tutorial_img_box">
                            <p class="text_color tutorial_box_title"> struktura </p>
                            <img src="~/assets/img/client_rozloz.png" class="tutorial_img">    
                        </div>
                        <p class="text_color normal_text">
                            Pokud vám některé složky nebo soubory chybí, tak si je vytvořte. A teď k jejich použití. <br>
                            Složka assets bude obsahovat složku, do které se budu ukládat obrázky receptů, zde si 
                            tuto složku pojmenujeme "img". <br> Ve složce components si vytváříme komponenty, ty nám 
                            zjednoduší zobrazení více souvisejicích dat. V tomto tutoriálu se využijí pro to, 
                            abychom zobrazily obrázek, název, ingredience  receptu a tlačítka pro interakci, jako jednu 
                            komponentu. <br> Ve složce layouts si můžeme vytvářet šablony, díky kterým se uživateli 
                            při prohlížení webu načítá pouze obsah samotné stránky a obsah šablony se načte pouze
                            jednou. <br>
                            Ve složce pages budou všechny stránky vašeho webu.
                        </p>
                    <h3 class="text_color title_text" id="nuxt-settings-id"> Nastavení Nuxtu </h3>
                        <p class="text_color normal_text">
                            V souboru "nuxt.config.js" si ve slovníku "axios:" nastavte "baseURL:" na 
                            "http://localhost:8000/vasprojekt". <br> Pokud chcete přechody mezi stránkami tak si 
                            také vytvořte ve složce assets složku "css" a v ní soubor "prechody.css". Cestu k 
                            tomuto souboru poté přidejte do seznamu "css:", cesta by měla vypadat takto: 
                            "~/assets/css/prechody.css"
                        </p>
                        <div class="tutorial_img_box">
                            <p class="text_color tutorial_box_title"> .../nuxt.config.js </p>
                            <img src="~/assets/img/nuxt_config.png" class="tutorial_img"> 
                        </div>
                        <div class="tutorial_img_box">
                            <p class="text_color tutorial_box_title"> .../assets/css/prechody.css </p>
                            <img src="~/assets/img/prechody.png" class="tutorial_img">   
                        </div>
                        <p class="text_color normal_text">
                            Dále si vytvořte ve složce store soubor "index.js", ve kterém bede logika
                            pro posílání requestu na recepty backendu a jejich uložení ve storu. Zároveň
                            zde bude logika pro zjišťování, zda je uživatel přihlášen a metoda pro jeho odhlášení
                        </p>
                        <div class="tutorial_img_box">
                            <p class="text_color tutorial_box_title"> .../store/index.js </p>
                            <img src="" class="tutorial_img">   <!-- přidat obrázek -->
                        </div>
                        <p class="text_color normal_text">
                            Také si vytvořte složku plugins, a v ní soubor "axios.js". Zde bude logika
                            pro modul axios
                        </p>
                        <div class="tutorial_img_box">
                            <p class="text_color tutorial_box_title"> .../store/index.js </p>
                            <img src="" class="tutorial_img">   <!-- přidat obrázek -->
                        </div>


                <h2 class="text_color title_text" id="pages-id"> Vytvoření stránek </h2>
                    <p class="text_color normal_text">
                        Nyní, když máme vše připraveno, si vytvoříme jednotlvé stránky.
                    </p>
                    <h3 class="text_color title_text" id="pages-layout-id"> Vytvoření layoutu </h3>
                        <p class="text_color normal_text">
                            Layout v tomto tutoriálu bude obsahovat 3 položky. První položka bude &lt;nav&gt;, 
                            který bude zobrazovat odkazy na jednotlivé stránky. Druhá položka bude &lt;main&gt;, 
                            zde se budou zobrazovat jednotlivé stránky. Třetí položkou je &lt;footer&gt;. <br>
                            Layout vytvořte ve složce layouts pod názvem default.vue a použíte pro něj následující kód: 
                        </p>
                        <div class="tutorial_img_box">
                            <p class="text_color"> .../client/layouts/default.vue </p>
                            <img src="~/assets/img/layout.png" class="tutorial_img">     <!-- přidat obrázek --> 
                        </div>
                        <p class="text_color normal_text">
                            V tomto layoutu je již i zahrnutá logika, pro správné zobrazování rozhraní pro 
                            přihlášené a nepřihlášené uživatele.
                        </p>
                    <h3 class="text_color title_text" id="pages-recipe-id"> Vytvoření stránky s recepty </h3>
                        <p class="text_color normal_text">
                            S hotovým layoutem si vytvořte ve složce pages soubor "index.vue", který bude stránka
                            zobrazující všechny recepty ve formě vytvořené ve "components/RecipeCard.vue". Kód stránky 
                            je v obrázku níže.
                        </p>
                        <div class="tutorial_img_box">
                            <p class="text_color"> .../client/pages/index.vue </p>
                            <img src="" class="tutorial_img">     <!-- přidat obrázek --> 
                        </div>
                        <p class="text_color normal_text">
                            Po stránce s recepty, si udělejte ve složce pages složku "_id". Pozor "_" je v názvu
                            nutné pro správnou funkci! V této složce vytvořte soubor "index.vue", který bude stránkou
                            pro zobrazení jendnoho receptu.
                        </p>
                        <div class="tutorial_img_box">
                            <p class="text_color"> .../client/pages/_id/index.vue </p>
                            <img src="" class="tutorial_img">     <!-- přidat obrázek --> 
                        </div>
                        <p class="text_color normal_text">
                            Jako poslední z frontendu si vytvořte ve složce pages soubor "add.vue". Tento soubor
                            bude stránkou pro přidání nového receptu.
                        </p>
                        <div class="tutorial_img_box">
                            <p class="text_color"> .../client/pages/add.vue </p>
                            <img src="" class="tutorial_img">     <!-- přidat obrázek --> 
                        </div>
                        <p class="text_color normal_text">
                            Nyní s připraveným frontendem je potřeba vytvořit potřebnou logiku na našem backendu.
                            Jelikož již máme vytvořené všechny potřebné routy, tak je potřeba už nastavit jen 
                            samotnou funkci v souboru views.py.
                        </p>
                        <div class="tutorial_img_box">
                            <p class="text_color"> .../vaseaplikace/views.vue </p>
                            <img src="" class="tutorial_img">     <!-- přidat obrázek --> 
                        </div>
                        <p class="text_color normal_text">
                            U receptů si vytvoříme ještě serializér v souboru serializers.py
                        </p>
                        <div class="tutorial_img_box">
                            <p class="text_color"> .../vaseaplikace/serializers.vue </p>
                            <img src="" class="tutorial_img">     <!-- přidat obrázek --> 
                        </div>
                    <h3 class="text_color title_text" id="pages-register-id"> Vytvoření stránky pro registraci </h3>
                        <p class="text_color normal_text">
                            Nyní na vytvoření stránky pro registraci. Ve frontendu je potřeba vytvořit stránku ve 
                            složce pages, nazveme ji "register.vue".
                        </p>    
                        <div class="tutorial_img_box">
                            <p class="text_color"> .../client/pages/register.vue </p>
                            <img src="" class="tutorial_img">     <!-- přidat obrázek --> 
                        </div>
                        <p class="text_color normal_text">
                            Jako další si k této stánce vytvořte v backendu funkci pro vyhodnocení registrace, 
                            ve složce views.py.
                        </p>
                        <div class="tutorial_img_box">
                            <p class="text_color"> .../vaseaplikace/views.py </p>
                            <img src="" class="tutorial_img">     <!-- přidat obrázek --> 
                        </div>
                    <h3 class="text_color title_text" id="pages-login-id"> Vytvoření stránky pro přihášení </h3>
                        <p class="text_color normal_text">
                            Nyní si ve frontendu ve složce pages vytvořte soubor stránky pro přihlášení. Nazveme ho 
                        </p>
                    
            </div>
            <div class="other">
                <!-- menu ostatních věcí -->
                <div class="switch-container">  <!-- darkmode toggle -->
                    <label class="switch">
                        <input type="checkbox" id="modeSwitch" @change="toggleDarkMode"/>
                        <span class="slider round"></span>
                    </label>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
  data() {
    return {
      placeholderFlex: 0,
      isDarkMode: false,
    };
  },
  head() {
    return {
      title: "AJAX tutoriál"
    };
    },
    mounted() {     // vykoná se jak se otevře stránka
    window.addEventListener("scroll", this.handleScroll);
    },
    beforeDestroy() {      // vykoná se před odchodem ze stránky
        if (this.isDarkMode === true) {
            this.toggleDarkMode();      // cypne dakrmode
        }
    },
    destroyed() {       //  vykoná se po odchodu ze stránky
    window.removeEventListener("scroll", this.handleScroll);    
    },
    methods: {
        handleScroll() {    //  logika pro scrollování
            const site_body = this.$el.querySelector(".site_body");
            const links = this.$el.querySelector(".links");
            const content = this.$el.querySelector(".content");
            const other = this.$el.querySelector(".other");
            const offsetTop = site_body.offsetTop;
            const scrollTop = window.scrollY;

            if (scrollTop >= offsetTop) {       //  když .side_body vyjede na vrch obrazovky
                links.style.position = "fixed";
                other.style.position = "fixed";
                other.style.marginLeft = "90%"; //  nastavením position: fixed; ignorovaly divy nastavený flex: x%; hodnoty
                content.style.marginLeft = "15%";
                content.style.marginRight = "10%";
        } else {                              //  když .side_body není na vrchu obrazovky
                links.style.position = "sticky";
                other.style.position = "sticky";
                other.style.marginLeft = "0";   // divy používají flex: x%; => margin není potřeba
                content.style.marginLeft = "0";
                content.style.marginRight = "0";
        }
        },
        toggleDarkMode() { // tutorial_img_box  tutorial_box_title
            this.isDarkMode = !this.isDarkMode;
            document.body.classList.toggle("dark-mode", this.isDarkMode);
            document.body.classList.toggle("light-mode", !this.isDarkMode);
            const site_body = this.$el.querySelector(".site_body");
            const div1 = this.$el.querySelector(".div1");
            const dark_switch = this.$el.querySelector(".switch");
            const img_box = this.$el.querySelectorAll(".tutorial_img_box");
            const img_title = this.$el.querySelectorAll(".tutorial_box_title");
            const textElements = this.$el.querySelectorAll(".text_color");  // querySelectorAll protože querySelector vzal jen text z 1 divu
            const top_nav = document.querySelectorAll(".top_nav_color");    // class .top_nav_color je v layoutu -> potřeba použít document
                                                                            // querySelector() by vybral pouze 1 odkaz -> potřeba použít querySelectorAll()

            if (this.isDarkMode === false) {        //  nastavení barviček pro lightmode
                site_body.style.backgroundColor = "#FFFFFF";
                div1.style.backgroundColor = "#BDBDBD";
                dark_switch.style.backgroundColor = "#FFFFFF";
                textElements.forEach((text) => {    //  nastaví barvu všeho textu (querySelectorAll => více prvků)
                    text.style.color = "#000000";
                });
                top_nav.forEach((li) => {       // nastaví barvu odkazů z layoutu 
                    li.style.color = "#000000";
                });
                img_box.forEach((box) => {       
                    box.style.border = "4px solid #000000";
                });
                img_title.forEach((title) => {       
                    title.style.backgroundColor = "#BDBDBD";
                });
                document.body.style.backgroundColor = "#FFFFFF";    //  body je basic struktura html => document
                document.querySelector('footer').style.backgroundColor = "#BDBDBD"; //  podobný jak body, jen specifikuju footer
        } else {                                  //  nastavení barviček pro darkmode
                site_body.style.backgroundColor = "#100F0E";
                div1.style.backgroundColor = "#757373";
                dark_switch.style.backgroundColor = "#100F0E";
                textElements.forEach((text) => {    //  nastaví barvu všeho textu (querySelectorAll => více prvků)
                    text.style.color = "#DFDFDF";
                });
                top_nav.forEach((li) => {       // nastaví barvu odkazů z layoutu 
                    li.style.color = "#DFDFDF";
                });
                img_box.forEach((box) => {       
                    box.style.border = "4px solid #DFDFDF";
                });
                img_title.forEach((title) => {       
                    title.style.backgroundColor = "#757373";
                });
                document.body.style.backgroundColor = "#100F0E";
                document.querySelector('footer').style.backgroundColor = "#757373"
            }
        },
        scrollToSection(sectionId) { // kotva odkaz bez změny URL adresy
            event.preventDefault();
            const section = document.getElementById(sectionId);
            if (section) {
                section.scrollIntoView({ behavior: 'smooth' });
            }
        }
  },
};
</script>

<style>

body {
    background-color: #FFFFFF;
}

.div1 {
    background-color: #BDBDBD;
    min-height: 50px;
}

.site_body{
    display: flex;
    overflow: hidden;
    position: relative;
    background-color: #FFFFFF;
}

.content{
    flex: 75%;
    overflow-y: auto;
}
.content::-webkit-scrollbar{
    width: 0;
}

.links,
.other{
    text-align: left;
    min-height: 100vh;
    z-index: 1;
    top: 0;
}
.links{
    flex: 15%;
    padding-left: 15px;
}
.other{
    flex: 10%;   
    padding-left: 20px;
}

.link_t{
    padding-bottom: 0;
}

.link_t_h2{
    font-size: 20px;
    font-weight: 600;
}

.link_t_h3{
    font-size: 15px;
}

img {
  max-width: 600px;
}

.text_color {
    color: black;
}

.normal_text{
    text-align: left;
}

.title_text{
    text-align: left;
}

.switch-container {
  display: flex;
  align-items: center;
  padding-top: 10px;
}

.switch {
  position: relative;
  display: inline-block;
  width: 60px;
  height: 34px;
}

.switch input {
  opacity: 0;
  width: 0;
  height: 0;
}

.slider {
  position: absolute;
  cursor: pointer;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: #BDBDBD;
  -webkit-transition: 0.4s;
  transition: 0.4s;
  border-radius: 34px;
}

.slider:before {
  position: absolute;
  content: '';
  height: 26px;
  width: 26px;
  left: 4px;
  bottom: 4px;
  background-color: #FFFFFF;
  -webkit-transition: 0.4s;
  transition: 0.4s;
  border-radius: 50%;
}

.dark-mode .slider:before {     /* nastavení barviček protože querySelector nevybere pseudoelement :before, nebo nevím jak ho vybrat */
  background-color: #100F0E;
}

.light-mode .slider:before {    /* nastavení barviček protože querySelector nevybere pseudoelement :before, nebo nevím jak ho vybrat */
  background-color: #FFFFFF;
}

input:checked + .slider {
  background-color: #757373;
}

input:checked + .slider:before {
  -webkit-transform: translateX(26px);
  -ms-transform: translateX(26px);
  transform: translateX(26px);
}

.page_link {
    font-weight: 500;
}

.tutorial_img_box {
    border: 4px solid #000000;
    border-radius: 10px;
    margin: 10px auto; 
    min-width: 10%;
    display: inline-block;
    box-sizing: border-box; /* Include padding and border in the width */
}

.tutorial_box_title {
    margin-bottom: 0px;
    background-color: #BDBDBD;
}

.tutorial_img {
    display: block;
    margin: 0 auto; 
    max-width: 100%; /* Ensure image does not overflow the container */
}

</style>