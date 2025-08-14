export interface HeaderStyles {
    background: string;
    textColor: string;
    borderColor: string;
    gradientFrom: string;
    gradientTo: string;
    underlineFrom: string;
    underlineTo: string;
}

export interface HeaderConfig {
    id: string;
    imageUrl: string;
    name: string;
    titles: string[];
    staticTitle: string;
    styles: HeaderStyles;
}

export const defaultStyles: HeaderStyles = {
    background: 'bg-gradient-to-br from-gray-900 via-gray-800 to-gray-900',
    textColor: 'text-white',
    borderColor: 'border-indigo-500/30',
    gradientFrom: 'from-blue-400',
    gradientTo: 'to-purple-500',
    underlineFrom: 'from-blue-500',
    underlineTo: 'to-purple-600'
};

export const defaultHeaderConfig: HeaderConfig = {
    id: 'header',
    imageUrl: '/assets/Main.jpg',
    name: 'Andrew Gubchenko',
    titles: [
        "Студент 2-го курса ДВГУПС",
        "Web-разработчик",
        "Разработчик Telegram-ботов",
        "Fullstack разработчик"
    ],
    staticTitle: "Fullstack разработчик",
    styles: { ...defaultStyles }
};