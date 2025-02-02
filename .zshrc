# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

EDITOR="nvim"

alias wifi="nmtui"
alias wf="nmtui"
alias vim=$EDITOR
alias v="$EDITOR"
alias ls="eza -a"
alias exti="exit"
alias xeit="exit"
alias eixt="exit"

# Git
alias gs="git status"
alias gc="git commit"
alias ga="git add"
alias gl="git log"
alias gd="git diff"

alias rss="newsboat"
alias mail="neomutt"
alias monitoron="xrandr --output HDMI-1 --mode 1920x1080 --rate 120 --right-of eDP-1"
alias zathura="devour zathura"
alias z="devour zathura"
alias mpv="devour mpv"

alias dotfiles='/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME'
alias dfiles='/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME'
alias ds='dotfiles status'
alias dc='dotfiles commit'
alias da='dotfiles add'
alias dl='dotfiles log'
alias ddiff='dotfiles diff'

alias cnvim="nvim ~/.config/nvim/lua/config"
alias cwm="$EDITOR ~/.config/qtile/config.py"
alias csh="$EDITOR ~/.zshrc"
alias cterm="$EDITOR ~/.config/alacritty/alacritty.toml"
alias crofi="$EDITOR ~/.config/rofi/config.rasi"
alias crss="$EDITOR ~/.config/newsboat"

# University
alias ut="cd ~/Documents/utfpr/"
alias riscv="devour java -jar ~/Documents/utfpr/arqcomp-elew30/rars1_6.jar"
alias wave="devour gtkwave"

# Work
alias qr="devour zathura ~/work/qr.pdf"

#Tmux
TMUX_CONFIG="~/.config/tmux/.tmux.conf"
alias tn="tmux -u -f $TMUX_CONFIG new"
alias ta="tmux -u -f $TMUX_CONFIG attach"
alias ctmux="$EDITOR $TMUX_CONFIG"
alias work="~/.config/tmux/tmux-base"

# The following lines were added by compinstall
zstyle ':completion:*' completer _complete _ignored
zstyle ':completion:*' glob 1
zstyle :compinstall filename '/home/murilo/.zshrc'

autoload -Uz compinit
compinit
# End of lines added by compinstall
#
# Lines configured by zsh-newuser-install
HISTFILE=~/.histfile
HISTSIZE=1000
SAVEHIST=1000
bindkey -v
# End of lines configured by zsh-newuser-install
source /usr/share/zsh-theme-powerlevel10k/powerlevel10k.zsh-theme

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh

export QT_QPA_PLATFORMTHEME=qt5ct
export QT_SELECT=5

PATH="$HOME/.local/bin:$PATH"
export npm_config_prefix="$HOME/.local"
