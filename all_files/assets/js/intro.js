
function intro() {
    const intro = introJs()
    intro.setOptions({
        steps: [
            {
                // element: '#one',
                intro: 'Welcome to DocHunt!! Let take a tour!!'
            },
            {
                element: '#one',
                intro: 'Here in "All Material" or in "Menu Bar" you can find all material stuff  !!'
            },
            {
                element: '#two',
                intro: 'This is where you get all updates!!'
            },
            {
                element: '#three',
                intro: 'here is some contact details'
            },
            {
                element: '#four',
                intro: 'You can follow me on insta and facebook from here and visit my website...'
            }
        ]
    })
    intro.start();
}