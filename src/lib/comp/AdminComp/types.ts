export interface Skill {
    id: number;
    title: string;
    description: string;
    icon: string;
    tags: string[];
}

export interface AboutSection {
    title: string;
    description: string;
    skills: Skill[];
}

export interface StyleSettings {
    primaryColor: string;
    secondaryColor: string;
    fontFamily: string;
    backgroundColor: string;
    textColor: string;
}

export interface SiteData {
    enabledComponents: string[];
    about: AboutSection;
    experience: Record<string, unknown>;
    header: Record<string, unknown>;
    footer: Record<string, unknown>;
    style: StyleSettings;
}