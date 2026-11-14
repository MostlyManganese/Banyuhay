# The script of the game goes in this file.


define a = Character("Juan", color="#4f7eff")
define b = Character("Maria", color="#4f7eff")
define c = Character("Doctor", color="#4f7eff")
define d = Character("Relative", color="#4f7eff")
define f = Character("idk4", color="#4f7eff")
define g = Character("", color="#4f7eff", window_background=None)
# The game starts here.

label start:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg kitchen

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    a "{i}It's only when I hear the sound of plates and utensils echoing from the kitchen that it makes me realize It's dinner time already.{/i}"

    a "{i}She's preparing dinner again.{/i}"

    a "{i}Even after working all day, she's still doing everything by herself.{/i}" with fade

    label kitchen:

    scene bg kitchen

    a "{i}Lately, she's been looking more weak and tired.{/i}"

    a "{i}What if she keeps pushing herself too hard?{/i}"

    a "{i}I fear that it'l make her condition worse...{/i}"

    a "{i}I need to have a talk with her.{/i}"


    label dining:

    scene bg dining

    b "Buti naman nakauwi ka na!"

    b "Naghanda ako ng paborito mong ulam, alam ko naman na pagod ka galing sa trabaho."

    a "Dapat nagpapahinga ka ngayon, alam mo naman yung sinabi ng doktor nung nakaraang bisita natin."

    b "Ayos lang ako. Sanay naman na ako sa gantong kalagayan ko."

    b "Kita mo naman na nagawa ko parin na maghanda ng piyesta, diba?"

    a "Hayy {i}wife name{/i}, ilang araw na kitang nakikitag pagod?"

    a "Minsan ang lala ng panghihingal mo. Hindi na pwedeng pabayaan yan na lumala."
    
    label dining2:

    scene bg dining

    b "Paulit-ulit ka na lang! Kita mo naman na kaya ko pa!" with hpunch

    b "Ganyan ba kaliit ang tingin mo sakin?" with hpunch

    a "{i}I don't want her to feel like a burden{/i}"

    menu:
        a "{i}What should I say next?{/i}"
        "Hindi ito tungkol sa kung kaya mo. Tungkol ito sa kalusugan mo!":
            jump bruh

        "Nag aalala lang ako sa kalagayan mo, ayokong lumala pa ito...":    
            jump test
    
    label bruh:

    a "Kapag pinagpatuloy mo pa, mas lalo pang lalala ang kondisyon mo!" with hpunch

    b "At pano naman tayo hahanap ng pambayad ng mga bayarin sa bahay kung hindi ako magtatrabaho?" with hpunch

    a "Ako na bahala, hindi mo na kailangang problemahin yun-"

    b "Itigil na natin ang usapang ito, lagi nalang tayong nag aaway."

    b "Bukas na natin toh problemahin, pagod tayong dalawa."

    b "Baka may masabi pa tayong hindi maganda sa isa't isa."

    label fall:

    scene bg dining

    a "{i}I don't like it when we fight like this. I don't want the day to end on a negative note...{/i}"

    b "{i}I'll make it up to her today.{/i}"

    "{i}plates crash{/i}"
    "{i}thud{/i}"
     

    a "Wife!!" with hpunch

    a "Wife anong ngyare sayo?!" with hpunch

    a "Tulong!" with hpunch

    label hospital:
    
    scene bg hospital

    c "Mabuti at naidala niyo po siya agad sa ospital."

    c "Ngunit kritikal na ang kalagayan ng iyong asawa."

    a "Hala dok, ano po ang gagawin namin ngayon?"

    c "Kailangan niyang sumailalim sa operasyon sa lalong madaling panahon."

    c "Kung hindi, maaaring lumala ang kanyang kalagayan."

    c "Pero malaki ang magiging gastusin para sa operasyon at gamutin, aabot ito sa mahigit-"
    #play sound buzz
    a "{i}Paano ko mababayaran ang lahat ng iyon?{/i}" with fade

    a "{i}Wala kaming ganoong kalaking pera.{/i}"
    return

    label test:

    scene bg dining

    a "Hindi ko kakayanin kung may mangyari sa'yo.."

    a "Ayoko ko pang mawala ka, gusto pa kita makasama habang buhay..."

    "{i}silence{/i}"

    b "Pasensya na..."

    b "Napapagod na rin kasi ako at nai-stress sa gastos natin."

    b "Ayokong nakikita kang magisa na naghihirap para lang matustus ang ating pamumuhay."

    a "Ako rin. Pero hindi natin kailangang harapin ito nang mag-isa."

    a "Mag-asawa tayo. Dapat magtulungan tayo."

    b "Tama ka."

    b "Pasensya na sa mga nasabi ko."

    a "Ako rin. Pasensya na kung napataas ang boses ko."


    b "Siguro kailangan ko na talagang bawasan ang trabaho ko."

    a "At tutulungan kita sa mga gawain dito sa bahay."

    b "Salamat."

    a "Ang mahalaga sa akin ay ang kalusugan mo."

    "{i}Nagngitian silang dalawa.{/i}"

    scene bg good

    "{i}HUG.{/i}" with hpunch


    return