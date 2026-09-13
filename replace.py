import os

files = [f for f in os.listdir('.') if f.endswith('.html')]
replacements = {
    '📍': '<i data-lucide="map-pin" class="icon-sm"></i>',
    '📞': '<i data-lucide="phone" class="icon-sm"></i>',
    '✉️': '<i data-lucide="mail" class="icon-sm"></i>',
    '📺': '<i data-lucide="youtube" class="icon-sm"></i>',
    '🕒': '<i data-lucide="clock" class="icon-sm"></i>',
    '✓': '<i data-lucide="check-circle" class="icon-sm"></i>',
    '💚': '<i data-lucide="heart" class="icon-md"></i>',
    '😊': '<i data-lucide="smile" class="icon-md"></i>',
    '🧩': '<i data-lucide="puzzle" class="icon-md"></i>',
    '🚀': '<i data-lucide="rocket" class="icon-md"></i>',
    '👩‍🏫': '<i data-lucide="users" class="icon-md"></i>',
    '🛡️': '<i data-lucide="shield" class="icon-md"></i>',
    '⭐⭐⭐⭐⭐': '<span style="display:inline-flex;gap:2px;color:#facc15;"><i data-lucide="star" class="icon-sm"></i><i data-lucide="star" class="icon-sm"></i><i data-lucide="star" class="icon-sm"></i><i data-lucide="star" class="icon-sm"></i><i data-lucide="star" class="icon-sm"></i></span>',
    '</head>': '<script src="https://unpkg.com/lucide@latest"></script>\n</head>'
}

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    for k, v in replacements.items():
        content = content.replace(k, v)
        
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print('Done!')
