package me.solofaze.HelloCommand;

import org.bukkit.command.Command;
import org.bukkit.command.CommandSender;
import org.bukkit.entity.Player;
import org.bukkit.plugin.java.JavaPlugin;

public class Main extends JavaPlugin {

	@Override
	public void onEnable() {  // server start state (needed for plugins)
		
	}
	@Override
	public void onDisable() {  // server stop state (needed for plugins)
		
	}
	
	// /hello <name> <amount>
	// <-- hey how are you!
	
	public boolean onCommand(CommandSender sender, Command cmd, String label, String[] args) {
		//hello
		if (label.equalsIgnoreCase("hello")) {
			
			if (sender instanceof Player) {
				Player player = (Player) sender;
				player.sendMessage("Hey me! How are you?");
				return true;
			} else {
				sender.sendMessage("Hey, how are you? NOT PLAYER!");
				return true;
			}
		}
		return false;
	}
}
	
