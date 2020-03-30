package me.solofaze.LaunchCommand;

import org.bukkit.command.Command;
import org.bukkit.command.CommandSender;
import org.bukkit.entity.Player;
import org.bukkit.plugin.java.JavaPlugin;

import net.md_5.bungee.api.ChatColor;


public class Main extends JavaPlugin {

	@Override
	public void onEnable() {
		
	}
	
	@Override
	public void onDisable() {
		
	}
	
	public boolean onCommand(CommandSender sender, Command cmd, String label, String[] args) {
		if (label.equalsIgnoreCase("launch") | label.equalsIgnoreCase("lch")) {
			if (!(sender instanceof Player)) {
				sender.sendMessage("*console goes flying*");
				return true;
			}
			Player player = (Player) sender;
			// /launch  / launch <number>
			if (args.length == 0) {
				// /launch
				player.sendMessage(ChatColor.LIGHT_PURPLE + "" + ChatColor.BOLD + "Zooooom!");
				player.setVelocity(player.getLocation().getDirection().multiply(2).setY(2));
				return true;
			}
			// /launch
			player.sendMessage(ChatColor.LIGHT_PURPLE + "" + ChatColor.BOLD + "Zooooom!");
			player.setVelocity(player.getLocation().getDirection().multiply(Integer.parseInt(args[0])).setY(2));
			return true;
		}
		return false;
	}
	
}
