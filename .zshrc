# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

alias vim="nvim"
alias v="nvim"
alias ls="exa -a"
alias gs="git status"
alias rss="newsboat"
alias monitoron="xrandr --output HDMI-1 --mode 1920x1080 --rate 120 --right-of eDP-1"
alias zathura="devour zathura"

alias dotfiles='/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME'

alias cnvim="nvim ~/.config/lua/config"
alias cwm="nvim ~/.config/qtile/config.py"
alias csh="nvim ~/.zshrc"
alias cterm="nvim ~/.config/alacritty/alacritty.yml"
alias crofi="nvim ~/.config/rofi/config.rasi"
alias crss="nvim ~/.config/newsboat"

# The following lines were added by compinstall

zstyle ':completion:*' completer _complete _ignored
zstyle ':completion:*' glob 1
zstyle :compinstall filename '/home/murilo/.zshrc'

autoload -Uz compinit
compinit
# End of lines added by compinstall
# Lines configured by zsh-newuser-install
HISTFILE=~/.histfile
HISTSIZE=1000
SAVEHIST=1000
bindkey -v
# End of lines configured by zsh-newuser-install
source /usr/share/zsh-theme-powerlevel10k/powerlevel10k.zsh-theme

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh
