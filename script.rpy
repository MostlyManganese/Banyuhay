# The script of the game goes in this file.


define a = Character("Mc", color="#4f7eff")
define b = Character("Wife", color="#4f7eff")
define c = Character("Doctor", color="#4f7eff")
define d = Character("Relative", color="#4f7eff")
define f = Character("idk4", color="#4f7eff")
define g = Character("", color="#4f7eff", window_background=None)
# The game starts here.

label start:
    stop music 
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

    a "Hindi ito tungkol sa kung kaya mo. Tungkol ito sa kalusugan mo!" with hpunch

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

    label hospital2:
    
    scene bg hospital

    a "Mahal, mabuti na mas okay na ang iyong kalagayan ngayon."

    b "Ano ang sabi ng doktor?"
    label black:

    scene bg black

    "{i}Man explains what the doctor said to him{/i}" with fade

    label hospital3:

    scene bg hospital

    b "Ang laki naman ng gastusin para sa operasyon.."

    b "Saan tayo kukuha ng ganoong kalaking pera? Lalo't na hindi ako makakatulong sayo."

    a "Huwag kang mag-alala maha."

    a "Gagawin ko ang lahat para makahanap ng paraan"

    b "Basta huwag kang gagawa na kung ano mang kalokohan para sa akin."

    b "Mas gugustuhin ko pang mamatay kaysa mapahamak ka."

    a "Hindi ako sasali sa mga masama o delikadong sitwasyon."

    a "Magtiwala ka sakin, hindi ko gagawin ang mga iyon." with fade

    label hospital4:
    
    scene bg hospital

    play sound "audio/phone.mp3" loop volume 0.4
    "{i}You hear the doorbell ring{/i}" with hpunch

    menu:
        "Open the door":
            "{i}You gently open the door{/i}"
            pass
    stop sound

    d "Kamusta na si *Name drop*?"

    a "Hindi parin maganda ang kanyang kalagayan niya."

    a "Mas lumala ang kanyang kondisyon pagkatapos ng heart attack na natamo niya"

    d "Nabalitaan ko ang nangyari kaya dumiretso na agad ako rito."

    a "Salamat talaga sa pagpunta mo rito, pasensya na rin kung biglaan."

    d "Ano ba ang sabi ng doktor?"

    d "May pagasa naman siyang gumaling diba?"

    a "Oo, pero malaki ang gastusin ang kailangang bayaran."

    d "Pano na yan? May pagkukuhaan ka ba ng pera?"

    a "Hindi ko pa alam pero gagawan ko ng paraan."

    "{i}silence."
    
    d "May naitabi akong kaunting pera, kunin mo na."

    d "Para rin ito kay *wife name drop*, wag mo na alalahanin ang pagbalik nito."
    

    menu:
        a "{i}Ayokong maging pabigat pero kinakailan ko lahat ng tulong sa ngayon. Ano ang pipiliin ko?{/i}"
        "Accept":
            a "Sigurado ka ba diyan?"

            d " Oo naman, para to kay *wife name drop*."

            d "Huwag mong kalimutan na may taong handang tumulong para sayo."

            a "Maraming salamat talaga *relative name drop*!"

            a "Gagawa ako ng paraan para makabawi sayo"

            d "Wala lang yan *man name drop"

            d "Huwag kang mawalan ng pag asa" with fade

        "Reject":
            pass
return
